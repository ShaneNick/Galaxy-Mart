from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer


User = get_user_model()

class SignupView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        # Create an instance of the UserLoginSerializer with the request data
        serializer = UserLoginSerializer(data=request.data)

        # If the serializer data is valid (email and password are correct)
        if serializer.is_valid():
            # Return a successful response with the validated data (access and refresh tokens)
            return Response(serializer.validated_data)

        # If the serializer data is invalid (email or password is incorrect)
        # Return a 400 Bad Request response with the serializer errors
        return Response(serializer.errors, status=400)
    


from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'middle_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            middle_name=validated_data.get('middle_name', ''),  # Handle optional middle name
            last_name=validated_data['last_name'],
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Retrieve the email and password from the input data
        email = data.get('email')
        password = data.get('password')

        # Query the database to find the user with the provided email
        user = User.objects.filter(email=email).first()

        # If a user is found and the provided password matches the user's password
        if user and user.check_password(password):
            # Generate a new JWT refresh token for the user
            refresh = RefreshToken.for_user(user)

            # Add the refresh and access tokens to the validated data
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            # Return the validated data with the tokens
            return data

        # If the email or password is invalid, raise a ValidationError
        raise serializers.ValidationError('Invalid email or password')
    


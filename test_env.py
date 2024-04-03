import os
from dotenv import load_dotenv

load_dotenv()  # explicitly load .env file

print(os.getenv('DATABASE_NAME'))
print(os.getenv('DATABASE_USER'))
print(os.getenv('DATABASE_PASSWORD'))
print(os.getenv('DATABASE_HOST'))
print(os.getenv('DATABASE_PORT'))

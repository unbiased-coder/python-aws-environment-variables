import os
from dotenv import load_dotenv

def lambda_entry(event, context):
    load_dotenv()
    print(f'Test variable is: {os.getenv("TEST_VARIABLE")}')
    print(f'Test variable 2 is: {os.getenv("TEST_VARIABLE_2")}')
    os.putenv('TEST_VARIABLE', '3')
    print(f'Test variable after edit: {os.getenv("TEST_VARIABLE")}')
    os.unsetenv('TEST_VARIABLE')
    print(f'Test variable after deletion: {os.getenv("TEST_VARIABLE")}')


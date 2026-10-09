from dotenv import load_dotenv # library that lets you load .env files, install with "pip install dotenv"
import os

#load_dotenv()
load_dotenv("./.env.user") #loads the contesnt of .env.user

username=os.environ.get("USER_NAME") #reads the environment variable USER_NAME

print("hello, {}".format(username))
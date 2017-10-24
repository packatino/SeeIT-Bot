from twython import Twython

import os
import sys

API_KEY_ENV = 'API_KEY'
API_KEY = os.environ.get(API_KEY_ENV)
if API_KEY is None:
    sys.exit("Error: Could not find " + API_KEY_ENV + " in environment variables.")

API_SECRET_ENV = 'API_SECRET'
API_SECRET = os.environ.get(API_SECRET_ENV)
if API_SECRET is None:
    sys.exit("Error: Could not find " + API_SECRET_ENV + " in environment variables.")

ACCESS_TOKEN_ENV = 'ACCESS_TOKEN'
ACCESS_TOKEN = os.environ.get(ACCESS_TOKEN_ENV)
if ACCESS_TOKEN is None:
    sys.exit("Error: Could not find " + ACCESS_TOKEN_ENV + " in environment variables.")

ACCESS_TOKEN_SECRET_ENV = 'ACCESS_TOKEN_SECRET'
ACCESS_TOKEN_SECRET = os.environ.get(ACCESS_TOKEN_SECRET_ENV)
if ACCESS_TOKEN_SECRET is None:
    sys.exit("Error: Could not find " + ACCESS_TOKEN_SECRET_ENV + " in environment variables.")

twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_client.update_status(status="Hello Universe!")

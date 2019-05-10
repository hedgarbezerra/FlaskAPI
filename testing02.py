import random
import string
from werkzeug.security import check_password_hash, generate_password_hash
import requests
from pprint import pprint
import json

url = 'https://flask-api200.herokuapp.com/v2/users'
r = requests.get(url)
r = r.json()
pprint(r)

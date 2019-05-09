import random
import string
from werkzeug.security import check_password_hash, generate_password_hash
gen = string.ascii_letters + string.digits + string.ascii_uppercase

key = ''.join(random.choice(gen) for i in range(15))
#print(key)

passdb = '123'
userdb = 'hedgar'
hashdb = generate_password_hash(passdb)
passauth = '123'
useratuh = ''

print(check_password_hash(hashdb, passauth))

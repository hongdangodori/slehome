import hashlib
import random
import string

def encrypted_key():
	seed = string.ascii_letters + string.digits
	size = 32
	random_key = ''.join(random.choice(seed) for x in range(size))
	random_key_bytes = random_key.encode('utf-8')
	return hashlib.sha256(random_key_bytes).hexdigest()
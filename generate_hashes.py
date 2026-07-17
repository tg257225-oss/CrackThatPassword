import hashlib

password = "alteria"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())
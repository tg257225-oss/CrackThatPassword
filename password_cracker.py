user_hash_dict = {}


with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()

with open('username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash

for user, hash in user_hash_dict

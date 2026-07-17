import hashlib

user_hash_dict = {}
try:

    with open('common_passwords.txt', 'r') as f:
        common_passwords = f.read().splitlines()

    with open('username_hashes.txt', 'r') as f:
        text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash
    cracked_user = set()

    for password in common_passwords:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        for username, hash in user_hash_dict.items():
            if hashed_password == hash:
                print(f'HASH FOUND\n{username}:{password}')
                cracked_user.add(username)

    for username in user_hash_dict:
        if username not in cracked_user:
            print(f'HASH NOT FOUND\n{username}: Could not be cracked')


finally:
    input("\Press Enter to Exit...")
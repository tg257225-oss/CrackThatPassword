# CrackThatPassword
CrackThatPassword is a simple Python program (strictly Windows) that can be used to..crack passwords (quite obvious). This program only looks at SHA-256 hashes, so any other algorithm is safe I suppose. 
### ![Code Running](Assets/updatedcode.png)

## How does it work?
If someone were to hack a database that stores log-in information, that person would be able to see the usernames of several users and their hashes. These hashes are generated from hashing algorithms, which take plain text passwords (something like 'password!') and scrambles them, making the information harder to steal. People have obviously found ways around this, figuring out how to turn the hashes back into plain text. This is exactly what this python program does! It reads a list of usernames and their hashes ('username_hashes.txt), turns a bunch of common passwords into hashes ('common_passwords.txt'), and checks to see if any of the hashes from the common passwords list matches up with any hashes in the list of usernames and hashes.

## How to use it (plsuseitethically)
Unzip the 'passwordcracker.zip'. Then, you can add any other common passwords into the 'common_passwords.txt' file and whatever username + hash combos you have into 'username_hashes.txt' (needs to be scrambled with SHA-256 algorithm). Finally, run the executable and the program will tell you if it found any passwords (or if it didn't).

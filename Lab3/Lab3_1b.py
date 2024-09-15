# Test whether cryptography was installed
# 
# Name: Keane Kouchi
# Date: 9/11/24


from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

message = input("Please enter a message:")
#message = b"This is a test message."
encoded = message.encode()

encrypted = f.encrypt(encoded)

decrypted = f.decrypt(encrypted)

print("Original message:", message)
print("Cipher text:", encrypted)
print("Decrypted message:", decrypted.decode())
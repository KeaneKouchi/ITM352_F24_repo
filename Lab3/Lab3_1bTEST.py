# Test whether cryptography was installed
# 
# Name: Keane Kouchi
# Date: 9/11/24



from cryptography.fernet import Fernet

def FernetEncrypt(input):
    key = Fernet.generate_key()
    f = Fernet(key)
    
    encoded = UserInput.encode()
    encrypted = f.encrypt(encoded)
    decrypted = f.decrypt(encrypted)
    decoded = decrypted.decode
    print("Original message:", UserInput)
    print("Cipher text:", encrypted)
    print("Decrypted message:", decrypted.decode())
    return key, encrypted, decoded

UserInput = input("Please enter a message to be encrypted and decrypted:")

DecryptMSG = FernetEncrypt(UserInput)

encoded, encrypted, decrypted, decoded = FernetEncrypt(UserInput)

DecryptMSG
#print("You entered:" , UserInput)
#print("This encrypted is: ", encrypted)
#print("This decrypted is: ", decoded)
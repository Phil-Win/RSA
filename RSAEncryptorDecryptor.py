#Overview: This program will take a modulus, message, and encryption key(or modulus, encrypted message and decryption key) and encrypt your message(or decrypt your encrypted message)

n,key,m,output = 0,0,0,0

n = int(input("What is your modulus? or your maximum number for your message?"))
key = int(input("Type in your key here.(Public encryption key to encrypt a message and private encryption key to decrypt a message)"))
m = int(input("What message do you plan on encrypting or decrypting?"))

output = (m**key) %n
print("Your encrypted/decrpted message has been printed below.")
print(output)

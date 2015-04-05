##Overview: This program will try to break the encryption by finding the decryption key (and decrypt a message) using 3 pieces of information
##your two public key information(modulus size and encryption key) along with the encrypted message

#Note: This won't actually work for companies that use an RSA encryption because they'll have modulus numbers where it would take too long to determine the prime factors

n,key,m,EulerTotient,d = 0,0,0,1,0

n = int(input("What is your modulus? or your maximum number for your message?"))
key = int(input("What is the public encryption key?"))
m = int(input("What message are you trying to decrypt?")) 
#This function will determine all prime factors of the number inputed(very inefficiently)
def listoffactors(n):
    lst = []
    while n %2==0:
        lst.append(2)
        n=n/2
    i = 3
    while i*i<=n:
        if n % i ==0:
            lst.append(i)
            n = n/i
            i = 3
        i+=2
    lst.append(int(n))
    return lst
#This section is effectively the Euler Totient function of your modulus
lst = listoffactors(n)
print("Prime factors that let's us break the code = ", lst)
for i in lst:
    EulerTotient *= (i-1)
print(EulerTotient)

#A property of the decryption key is that it's the multiplicative inverse of your encryption key.. mod the Euler TOtient number. This loop brute force finds that number 
for i in range(1,EulerTotient):
    if  (key * i) % EulerTotient ==1:
        d = i
print("The decryption key is...")
print(d)
print("The message decrypted is...")
print((m**d) % n)



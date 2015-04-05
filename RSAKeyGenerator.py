#Overview: Since the primary way to break an RSA encrypion is through finding divisors of your modulus,
#this program will force you to have a modulus with exactly 4 divisors(2 prime numbers, 1, and the number itself) which will be hard to break
#After finding your modulus, the program will have you pick a valid encryption key and then it will calculate the decryption key.

p,q,n,EulerTotient,e,d = 0,0,0,0,0,0
import fractions

#This function will ensure a number  you input is prime
def isPrime(x):
  if x==2:
    return True
  if x%2==0:
    return False
  i = 3
  while i**2<=x:
    if x % i == 0:
      return False
    i+=2
  else:
    return True

print("To come up with a key, you need to have two large distinct primes prepared")
p = int(input("Enter your first prime number here. (Make sure it is larger than 1)"))

while not (isPrime(p) and p>1):
  p = int(input("The number you picked is not a prime number larger than 1. Try again"))
  
q = int(input("Enter your second prime number here. (Make sure it is larger than 1)"))

while not (isPrime(q) and q>1):
  q = int(input("The number you picked is not a prime number larger than 1. Try again"))  

n = p * q
EulerTotient = (p-1) * (q-1)

print("Now we need to pick our encryption key. It needs to follow two criteria.")
print("1. The greatest common denominator between the number you pick and %d needs to be 1" % (EulerTotient))
print("2. It must be between 1 and %d" % (EulerTotient))
print("Don't worry, I'll check to make sure you pick a good number")
e = int(input("Enter  your encryption key here"))
while (e<=1 or e>=EulerTotient or fractions.gcd(e,EulerTotient)!=1):
  e = int(input("Sorry, the number you picked does not follow the criteria listed. Try again"))

for i in range(0,EulerTotient):
  if (i*e) % EulerTotient == 1:
    d = i
    break

print("Here is your public key information")
print("Modulus:", n)
print("Encryption key:", e)
print("Here is your private key information")
print("Decryption key:", d)
print("Do NOT leak/share the private key or prime numbers used to anyone")



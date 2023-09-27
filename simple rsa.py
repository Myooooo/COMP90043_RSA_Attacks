# Importing the required libraries for RSA demonstration
from random import randint
import sympy

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """Calculate the modular multiplicative inverse of a mod m."""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def is_coprime(a, b):
    """Check if a and b are coprime (i.e., GCD(a, b) = 1)."""
    return gcd(a, b) == 1

def generate_keypair(p, q):
    """Generate a pair of RSA keys."""
    # Calculate n = p * q
    n = p * q

    # Calculate the totient of n, phi(n) = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = randint(2, phi - 1)
    while not is_coprime(e, phi):
        e = randint(2, phi - 1)

    # Compute the modular multiplicative inverse d of e (mod phi(n))
    d = mod_inverse(e, phi)

    # Return the public and private keys
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypt a plaintext message using a public key."""
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    """Decrypt a ciphertext message using a private key."""
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

# Generate two distinct large prime numbers p and q
p = sympy.randprime(1000, 9999)
q = sympy.randprime(1000, 9999)
while p == q:
    q = sympy.randprime(1000, 9999)

# Generate RSA key pairs
public_key, private_key = generate_keypair(p, q)

# Sample plaintext message
plaintext = "HELLO"

# Encrypt the plaintext
ciphertext = encrypt(public_key, plaintext)

# Decrypt the ciphertext
decrypted_text = decrypt(private_key, ciphertext)





from sympy import isprime

def generate_large_primes(start, end, count):
    """
    Generate a list of large prime numbers within a given range and count.
    
    Parameters:
        start (int): The start of the range to look for primes.
        end (int): The end of the range to look for primes.
        count (int): The number of primes to generate.
    
    Returns:
        list: A list containing the generated prime numbers.
    """
    primes = []
    for num in range(start, end + 1):
        if len(primes) >= count:
            break
        if isprime(num):
            primes.append(num)
    return primes

# Generate 2 large prime numbers between 10^4 and 10^5 for RSA demonstration
generate_large_primes(10**4, 10**5, 2)

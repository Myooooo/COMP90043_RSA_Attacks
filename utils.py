import random

# return true if input number is a prime number
# n: input number
# k: Miller Rabin iterations
# time complexity O(klogn)
def isPrime(n, s=5):
    if(n <= 1):
        return False
    elif(n <= 3):
        return True
    elif(n%2 == 0):
        return False
    else:
        return millerRabin(n,s)

# return a random prime number from start to end
def randPrime(start=2, end=100):
    prime_candidate = random.randint(start, end)
    while not isPrime(prime_candidate):
        prime_candidate = random.randint(start, end)
    return prime_candidate

# return GCD of a and b
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

# extended euclidean algorithm
def xgcd(a, b):
    if a == 0:
        return b,0,1
    
    gcd,x,y = xgcd(b%a,a)

    m = y - (b//a) * x
    n = x

    return gcd,m,n

# return modular inverse of a mod n
# None if does not exist
def invMod(a, n):
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    return None

# return a^b mod n
# Introduction to Algorithms, 4th edition, p. 935
def modExp(a, b, n):
    if b == 0:
        return 1
    elif b % 2 == 0:
        # b is even
        d = modExp(a, b//2, n)
        return (d * d) % n
    else: 
        # b is odd
        d = modExp(a, b-1, n)
        return (a * d) % n

# Miller-Rabin primality test
# Introduction to Algorithms, 4th edition, p. 946
def millerRabin(n, s):
    for _ in range(s):
        a = random.randint(2, n-2)
        if witnessMR(a, n):
            return False
    return True

# Miller-Rabin primality test witness
# Introduction to Algorithms, 4th edition, p. 946
def witnessMR(a, n):
    t = 0
    u = n - 1
    while u % 2 == 0:
        t += 1
        u //= 2
    
    x = modExp(a, u, n)
    for _ in range(t):
        prev = x
        x = modExp(prev, 2, n)
        if x == 1 and prev != 1 and prev != n-1:
            return True
    if x != 1:
        return True
    return False
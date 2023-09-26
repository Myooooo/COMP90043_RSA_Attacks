# return true if input number is a prime number
def isPrime(n):
    # TO-DO
    return True

# return a random prime number from start to end
def randPrime(start=2, end=100):
    # TO-DO
    pass

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
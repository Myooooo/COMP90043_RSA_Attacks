import random
import utils

class RSA:
    def __init__(self, p=None, q=None, e=None):
        # check primalities of p and q if given
        # generate random p and q if not given
        if p is not None:
            assert(utils.isPrime(p), True)
        else:
            p = utils.randPrime(10, 1000)
        
        if q is not None:
            assert(utils.isPrime(q), True)
        else:
            q = utils.randPrime(10, 1000)

        # check primality of e if given
        if e is not None:
            assert(utils.isPrime(e), True)

        # store p, q
        self.p = p
        self.q = q
        
        # generate public and private keys
        self.pub_key, self.pri_key = self.keygen(e)
    
    # generate a random e that is odd and coprime with phi
    def rand_e(self, phi):
        while True:
            e = random.randrange(2, phi)
            if utils.gcd(e, phi) == 1 and e % 2 == 1:
                return e
            
    # generate the smallest valid e
    def smallest_e(self, phi):
        e = 3
        while True:
            if utils.gcd(e, phi) == 1:
                return e
            e += 2
    
    # key generation
    def keygen(self, e):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        
        if e is None:
            # randomly generate e if not given
            e = self.smallest_e(phi)
        else:
            # check if e is coprime with phi
            if utils.gcd(e, phi) != 1:
                raise Exception("e is not coprime with phi")
        
        d = utils.invMod(e, phi)

        return ((e, n), (d, n))
    
    # encryption
    def encrypt(self, m):
        e, n = self.pub_key
        c = [utils.modExp(ord(ch), e, n) for ch in m]
        return c

    # decryption
    def decrypt(self, c):
        d, n = self.pri_key
        m = [chr(utils.modExp(ch, d, n)) for ch in c]
        return ''.join(m)
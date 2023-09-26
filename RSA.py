import random
import utils

class RSA:
    def __init__(self, p, q, e=None):
        self.p = p
        self.q = q
        self.e = e

        # # check primalities of p and q
        # assert(utils.isPrime(p), True)
        # assert(utils.isPrime(q), True)

        # # check primality of e if given
        # if e is not None:
        #     assert(utils.isPrime(e), True)
        
        # generate public and private keys
        self.pub_key, self.pri_key = self.keygen()
    
    # generate a random e that is odd and coprime with phi
    def rand_e(self, phi):
        while True:
            e = random.randrange(2, phi)
            if utils.gcd(e, phi) == 1 and e % 2 == 1:
                return e
    
    # key generation
    def keygen(self):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        
        if self.e is None:
            # randomly generate e if not given
            self.e = self.rand_e(phi)
        else:
            # check if e is coprime with phi
            if utils.gcd(self.e, phi) != 1:
                raise Exception("e is not coprime with phi")
        
        d = utils.invMod(self.e, phi)

        return ((self.e, n), (d, n))
    
    # encryption
    def encrypt(self, m):
        e, n = self.pub_key
        c = [(ord(ch) ** e) % n for ch in m]
        return c

    # decryption
    def decrypt(self, c):
        d, n = self.pri_key
        m = [chr((ch ** d) % n) for ch in c]
        return ''.join(m)
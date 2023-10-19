import time
import statistics
from matplotlib import pyplot as plt

import utils
from RSA import RSA

class TimingAttack:
    def __init__(self, rsa):
        self.rsa = rsa
        self.pub_key = rsa.pub_key
    
    # return decryption time on c in ms
    def getDecryptTime(self, rsa, c):
        start_time = time.time_ns()
        rsa.decrypt(c)
        end_time = time.time_ns()
        return (end_time - start_time)/1000000
    
    # return average decryption time a m_char message over n trials in ms
    def getAvgDecryptTime(self, rsa, n=100, m_len=100):
        m = "a" * m_len
        c = rsa.encrypt(m)
        timings = []
        for _ in range(n):
            timings.append(self.getDecryptTime(rsa, c))
        return statistics.mean(timings)

    # perform timing attack
    def attack(self):
        # get key length in bits
        n_bits = self.rsa.pub_key[1].bit_length()
        timings = []

        for i in range(2, n_bits-1):
            # generate a valid pair of p,q
            while True:
                p = utils.randPrime(n_bits=i)
                q = utils.randPrime(n_bits=(n_bits-i))
                if (p * q).bit_length() == n_bits:
                    break

            e = 65537
            rsa = RSA(p,q,e)
            print("\nAnalysing p: {}bits".format(i))
            print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
            print("p: {}bits, q: {}bits, d: {}bits, n: {}bits".format(p.bit_length(), q.bit_length(), rsa.pri_key[0].bit_length(), (rsa.p*rsa.q).bit_length()))
            
            decrypt_time = self.getAvgDecryptTime(rsa)
            timings.append(decrypt_time)
            print("Decryption time: {}ms".format(decrypt_time))

        plt.plot(timings)
        plt.show()
        
# random p,q with defined bit length
p = utils.randPrime(n_bits=100)
q = utils.randPrime(n_bits=100)
e = 65537
rsa = RSA(p, q, e)

timingAttack = TimingAttack(rsa)
timingAttack.attack()
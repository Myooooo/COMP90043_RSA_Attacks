import time
import random
import statistics
from matplotlib import pyplot as plt
from tqdm import tqdm

import utils
from RSA import RSA

class TimingAttack:
    def __init__(self, rsa):
        self.rsa = rsa
        self.pub_key = rsa.pub_key
    
    # return decryption time on c in ns
    def getDecryptTime(self, c_num):
        start_time = time.time_ns()
        self.rsa.decrypt_int(c_num)
        end_time = time.time_ns()
        return (end_time - start_time)/1000
    
    # return average decryption time a m_char message over n trials in ns
    def getAvgDecryptTime(self, m_num, n_trails=10):
        c_num = self.rsa.encrypt_int(m_num)
        timings = []
        for _ in range(n_trails):
            timings.append(self.getDecryptTime(c_num))
        return statistics.mean(timings)

    # perform timing attack
    def attack(self, n_trials=1000):
        d_rec = 1
        n = self.pub_key[1]
        n_bits = n.bit_length()

        for i in range(1, n_bits):
            print("Analysing bit {}/{}".format(i, n_bits))

            Y_timings = []
            Z_timings = []

            for _ in tqdm(range(n_trials), ascii=False, ncols=100):
                Y = random.randint(1, int(n ** (1/3.0)))
                Z = random.randint(int(n ** (1/3.0)), int(n ** (1/2.0)))

                Y_timing = self.getAvgDecryptTime(Y)
                Z_timing = self.getAvgDecryptTime(Z)
                
                Y_timings.append(Y_timing)
                Z_timings.append(Z_timing)

            Y_mean = statistics.mean(Y_timings)
            Z_mean = statistics.mean(Z_timings)
            print(Y_mean, Z_mean)

            if Z_mean > Y_mean:
                # push 1
                d_rec = (d_rec << 1) | 1
            else:
                # push 0
                d_rec = d_rec << 1
            
            print("Recovered d: {}".format(bin(d_rec)))

        print(d_rec)
        
# random p,q with defined bit length
p = utils.randPrime(n_bits=100)
q = utils.randPrime(n_bits=100)
e = 65537
rsa = RSA(p, q, e)
print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
print("key length: {}bits".format((rsa.p*rsa.q).bit_length()))

timingAttack = TimingAttack(rsa)
timingAttack.attack()
import time
import random
import statistics
from tqdm import tqdm

# seed random generator for constant result
random.seed(88)

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
    def getAvgDecryptTime(self, m_num, n_trails=5):
        c_num = self.rsa.encrypt_int(m_num)
        timings = []
        for _ in range(n_trails):
            timings.append(self.getDecryptTime(c_num))
        return statistics.mean(timings)
    
    # returns the number of different bits between a and b
    def getDiffBits(self, a, b):
        # trim longer integer
        len_diff = a.bit_length() - b.bit_length()
        if len_diff > 0:
            a >>= len_diff
        else:
            b >>= -len_diff

        # XOR for different bits
        xor = a ^ b
        n = 0
        for _ in range(a.bit_length()):
            n += xor & 1
            xor >>= 1
        return n

    # perform timing attack
    def attack(self, n_trials=1000):
        d_rec = 1
        n = self.pub_key[1]
        n_bits = n.bit_length()

        start_time = time.time()

        # analyse by bits
        for i in range(1, n_bits):
            print("Analysing bit {}/{}".format(i, n_bits))

            Y_timings = []
            Z_timings = []

            # sample n trials
            for _ in tqdm(range(n_trials), ascii=False, ncols=100):

                # Y^3 < N, Z^2 < N < Z^3
                Y = random.randint(1, int(n ** (1/3.0)))
                Z = random.randint(int(n ** (1/3.0)), int(n ** (1/2.0)))

                # sample decryption times
                Y_timing = self.getAvgDecryptTime(Y)
                Z_timing = self.getAvgDecryptTime(Z)
                Y_timings.append(Y_timing)
                Z_timings.append(Z_timing)

            # compute mean time
            Y_mean = statistics.mean(Y_timings)
            Z_mean = statistics.mean(Z_timings)
            print(Y_mean, Z_mean)

            # compare mean time and push bit
            if Z_mean > Y_mean:
                # push 1
                d_rec = (d_rec << 1) | 1
            else:
                # push 0
                d_rec = d_rec << 1
            
            print("Recovered d: {}".format(bin(d_rec)))

        elapsed_time = time.time() - start_time
        print("\nTime elapsed: \t{}s".format(elapsed_time))
        print("Recovered d: \t{}".format(d_rec))
        print("Actual d: \t{}".format(self.rsa.pri_key[0]))
        print("Accuracy: \t{}%".format(self.getDiffBits(d_rec, self.rsa.pri_key[0]) / self.rsa.pri_key[0].bit_length() * 100))
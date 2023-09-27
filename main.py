import random
import time
import warnings

from RSA import RSA
import utils

random.seed(time.time())
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    # # random p,q,e
    # rsa = RSA()

    # given p,q
    p = 10921304574392093059217153525481121125933934477429
    q = 89855181341172893110764453512406142438324081807631
    rsa = RSA(p,q)

    # # given p,q,e
    # rsa = RSA(61, 53, 17)

    # # random p,q with defined range
    # p = utils.randPrime(1000, 10000)
    # q = utils.randPrime(1000, 10000)
    # rsa = RSA(p, q)

    print("p={}, q={}, n={}, e={}, d={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))

    m = "hello"

    start_time = time.time()
    c = rsa.encrypt(m)
    end_time = time.time()
    print("encryption time: {}s".format(end_time - start_time))

    start_time = time.time()
    decryped = rsa.decrypt(c)
    end_time = time.time()
    print("decryption time: {}s".format(end_time - start_time))

    print("message:", m)
    print("encrypted:", c)
    print("decrypted:", decryped)
import random
import time
import warnings

from RSA import RSA

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

    # random p,q with defined bit length
    # p = utils.randPrime(n_bits = 100)
    # q = utils.randPrime(n_bits = 100)
    # rsa = RSA(p, q)

    print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
    print("key length: {}bits".format((rsa.p*rsa.q).bit_length()))

    m = "hello"

    start_time = time.time_ns()
    c = rsa.encrypt(m)
    end_time = time.time_ns()
    print("encryption time: {}ms".format((end_time - start_time)/1000000))

    start_time = time.time_ns()
    decryped = rsa.decrypt(c)
    end_time = time.time_ns()
    print("decryption time: {}ms".format((end_time - start_time)/1000000))

    print("message:", m)
    print("encrypted:", c)
    print("decrypted:", decryped)
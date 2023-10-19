import utils
from RSA import RSA
from TimingAttack import TimingAttack

def main():
    # # random p,q,e
    # rsa = RSA()

    # # given p,q
    # p = 10921304574392093059217153525481121125933934477429
    # q = 89855181341172893110764453512406142438324081807631
    # rsa = RSA(p,q)

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

    # random p,q with defined bit length
    p = utils.randPrime(n_bits=100)
    q = utils.randPrime(n_bits=100)
    e = 65537
    rsa = RSA(p, q, e)

    print("\n>>> Creating RSA Scheme <<<\n")
    print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
    print("key length: {}bits".format((rsa.p*rsa.q).bit_length()))

    # perform timing attack
    print("\n>>> Performing timing attack <<<\n")
    timingAttack = TimingAttack(rsa)
    timingAttack.attack()

if __name__ == "__main__":
    main()
from RSA import RSA
import utils

if __name__ == "__main__":
    rsa = RSA(11, 17)

    print("p={}, q={}, n={}, e={}, d={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))

    m = "hello"
    c = rsa.encrypt(m)
    decryped = rsa.decrypt(c)

    print("message:", m)
    print("encrypted:", c)
    print("decrypted:", decryped)

    print(utils.isPrime(10921304574392093059217153525481121125933934477429))
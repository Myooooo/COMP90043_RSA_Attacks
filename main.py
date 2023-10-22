import utils
from RSA import RSA
from TimingAttack import TimingAttack
import BruteForce
import ChosenCipher

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
    p = utils.randPrime(n_bits=32)
    q = utils.randPrime(n_bits=32)
    e = 65537
    rsa = RSA(p, q, e)

    print("\n>>> Creating RSA Scheme <<<\n")
    print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
    print("key length: {}bits".format((rsa.p*rsa.q).bit_length()))

    # perform brute force attack
    print("\n>>> Performing brute force attack <<<\n")
    print("This will take about 2 hours to run 10 REPEAT times up to 30-bit RSA")
    print("Please modify the constant MAXBIT to see the impact of key length")
    BruteForce.attack()
    
    # perform Chosen Plaintext attack
    print("\n>>> Performing Chosen Plaintext attack <<<\n")
    ChosenCipher.CPA(p,q)
    
    # perform Chosen Ciphertext attack
    print("\n>>> Performing Chosen Ciphertext attack <<<\n")
    ChosenCipher.CCA(p,q)

    # perform timing attack
    print("\n>>> Performing timing attack <<<\n")
    print("NOTE: Timing might be messed up by docker environment.")
    print("Please run source code locally for better results.")
    timingAttack = TimingAttack(rsa, offset = 0.01)
    timingAttack.attack(n_trials = 100 * (rsa.p*rsa.q).bit_length())
    
if __name__ == "__main__":
    main()
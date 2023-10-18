import sys, os
import random
import math
import time
from sympy import *
from time import sleep
import matplotlib.pyplot as plt
import datetime
from string import ascii_letters, digits
import utils
from RSA import RSA

# function to factorize an integer n
def fac(n):
    max = math.ceil(math.sqrt(n))
    s = 3
    if n % 2 == 0:
        return 2, n//2
    
    while n % s != 0 and s < max:
        s = nextprime(s) 
        
    return s
    
    

def main():
    # Time taken for each bit length
    time_data = {}
    
    # Looping through different bit lengths
    for n_bits in range(30, 33):  # Example bit lengths 30, 31, 32
        # Start time
        start_time = time.time()
        
        # Generate n-bit prime numbers for p and q
        p = utils.randPrime(n_bits=n_bits)
        q = utils.randPrime(n_bits=n_bits)
        
        # Existing RSA and brute-force logic (To be filled in)
        # ...
        
        # End time
        end_time = time.time()
        
        # Calculate time taken
        time_taken = end_time - start_time
        
        # Store the time data
        time_data[n_bits] = time_taken
        
        print(f"Time taken for {n_bits}-bit RSA: {time_taken} seconds")
    
def main():
    #p = random.choice()
    p = 66424187
    q = 87006341
    #rsa = RSA(p,q)
    count = 10
    m = "random"
    time = []
    length = []
    #
    pqdict = [(3,5),(17,11),(191,173),(45659,59497),(236773,283741),(1024391,1003003),(13390961,10087351),(182468119,164535253)]
    #c = rsa.encrypt(m)
    for (p,q)in pqdict:
        start = datetime.datetime.now()
        p= fac(p*q)

        end = datetime.datetime.now()

        time.append((end-start).total_seconds())
        length.append(p.bit_length())
    print(time)
    plt.axis('auto')

    for i in range(len(length)):
        plt.annotate(str(length[i]),
    xy=(length[i], time[i]), xycoords='data',
    xytext=(5, 0), textcoords='offset points',
    size=7,
    bbox=dict(boxstyle="round4,pad=.5", fc="0.8", alpha=0.4),
    arrowprops=dict(arrowstyle="-"))
    plt.plot(length,time)
    plt.xlabel("Length(bits)")
    plt.ylabel("Time")
    plt.show()
    return 1
    



if __name__ == "__main__":
    main()
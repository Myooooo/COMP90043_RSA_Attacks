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

MINBIT = 2
MAXBIT = 31
REPEAT = 10.0

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
    # initialize the time count for n-bit RSA brute force decryption
    time_data = {}
    for bit in range(MINBIT, MAXBIT):
        time_data[bit] = 0
    
    i = 0
    while (i < REPEAT):
        test(time_data)
        i += 1
    
    for bit in range(MINBIT, MAXBIT):
        time_data[bit] /= REPEAT
    
    plt.axis('auto')

    for i in range(MINBIT, MAXBIT):
        plt.annotate(str(i),
    xy=(i, time_data[i]), xycoords='data',
    xytext=(5, 0), textcoords='offset points',
    size=7,
    bbox=dict(boxstyle="round4,pad=.5", fc="0.8", alpha=0.4),
    arrowprops=dict(arrowstyle="-"))
    plt.plot(time_data.keys(),time_data.values())
    plt.xlabel("Length(bits)")
    plt.ylabel("Time")
    plt.show()
    
def test(time_data):
    # Looping through different bit lengths
    for n_bits in range(MINBIT, MAXBIT):

        # Generate n-bit prime numbers for p and q
        p = utils.randPrime(n_bits=n_bits)
        q = utils.randPrime(n_bits=n_bits)
        
        start_time = time.time()
        p= fac(p*q)
        end_time = time.time()
        
        # Calculate time taken
        time_taken = end_time - start_time
        
        # Store the time data
        time_data[n_bits] += time_taken
        
        print(f"Time taken for {n_bits}-bit RSA: {time_taken} seconds")

if __name__ == "__main__":
    main()
import sys, os
import random
import math
from sympy import *
from time import sleep
import matplotlib.pyplot as plt
import datetime
from string import ascii_letters, digits
from RSA import RSA
    
def fac(n):
    max = math.ceil(math.sqrt(n))
    s = 3
    if n % 2 == 0:
        return 2, n//2
    
    while n % s != 0 and s < max:
        s = nextprime(s) 
        
    return s
    
    
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
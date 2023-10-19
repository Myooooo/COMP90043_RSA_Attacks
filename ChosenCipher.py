import sys, os
import random
import math
from sympy import *
from time import sleep
import matplotlib.pyplot as plt
import datetime
from string import ascii_letters, digits
from RSA import RSA
import utils
def CPA(p, q):

    rsa = RSA(p, q)
    print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
    m = random.randrange(100, 1000)
    c = utils.modExp(m,rsa.pub_key[0], rsa.pub_key[1])
    print('Alice sends m = {} to Bob as m^e = {}'.format(m, c))
    print('Bob decrypts c = {} to m = c^d = {}'.format(c,utils.modExp(c,rsa.pub_key[0], rsa.pub_key[1])))


    for t in range(100,1000):
        if utils.modExp(t,rsa.pub_key[0], rsa.pub_key[1])== c:
            print('Eve has found the message: {}'.format(t))
    
    
def CCA(p,q):
    rsa = RSA(p, q)
    print("p={}\nq={}\nn={}\ne={}\nd={}".format(rsa.p, rsa.q, rsa.pub_key[1], rsa.pub_key[0], rsa.pri_key[0]))
    m = random.randrange(100, 1000)
    c = utils.modExp(m,rsa.pub_key[0], rsa.pub_key[1])
    print('Alice sends m = {} to Bob as m^e = {}'.format(m, c))
    print('Eve intercepts c, modifies c by c * 2^e and sends cb to bob')
    
    evep = 2
    ca = utils.modExp(2,rsa.pub_key[0], rsa.pub_key[1])
    cb = c*ca % rsa.pub_key[1]
    cbd = (utils.modExp(c,rsa.pri_key[0], rsa.pub_key[1]) * utils.modExp(ca,rsa.pri_key[0], rsa.pub_key[1])) % rsa.pub_key[1]
    print('Bob decrypts cb = {} to  cb^d = {}'.format(cb, cbd))
    print('cb^d = m*2, therefore m = {}'.format(cbd/2))
    
   
    
def main():
    p = 66424187 #can be randomly chosen
    q = 87006341
    #CCA(p,q)
    CPA(p,q)
    
if __name__ == "__main__":
    main()

    

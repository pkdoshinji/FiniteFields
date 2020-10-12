#!/usr/bin/env python3

'''
Python class for computation over a finite field of order p, where
p is prime.

Author: Patrick Kelly
Email: patrickyunen@gmail.com
Last revised: October 12, 2020
'''


from random import randint

class FField:

    def __init__(self, prime, number):
        self.order = prime
        self.value = number
        if self.fermat_test(self.order) == False:
            print('Field order must be prime!')
            exit()

    def __str__(self):
        return str(self.value) + f' ∊ GF({self.order})'

    def __add__(self, other):
    #Addition over a finite field of prime order
        return FField(self.order, (self.value + other.value) % self.order)

    def __sub__(self, other):
    #Subtraction over a finite field of prime order
        return FField(self.order, (self.value - other.value) % self.order)

    def __mul__(self, other):
    #Multiplication over a finite field of prime order
        return FField(self.order, (self.value * other.value) % self.order)

    def __pow__(self, integer):
    #Exponentiation over a finite field of prime order
        return FField(self.order, (self.value ** integer) % self.order)

    def __truediv__(self, other):
    #Division over a finite field of prime order
        return FField(self.order, (self.value * other.inverse().value) % self.order)

    def inverse(self):
    #Get the inverse of n ∊ GF(p) using the (p-2) algorithm
        return self.__pow__(self.order - 2)

    def mr_test(self, candidate, s=10):
    #Miller-Rabin primality test for a candidate prime
        if candidate == 2:
            return True
        if candidate % 2 == 0:
            return False
        u, r = decompose(candidate - 1)
        alpha = randint(2, (candidate - 2))
        z = pow(alpha, r, candidate)
        if z != 1 and z != (candidate - 1):
            for j in range(1, u):
                z = (z ** 2) % candidate
                if z == 1:
                    return False
            if z != (candidate - 1):
                return False
        return True

    def decompose(self, p):
    #Given an odd p, decompose p-1 as (2 ** u)(r) where r is odd
        u = 0
        while (p % 2) == 0:
            u += 1
            p //= 2
        return twos, int(p)

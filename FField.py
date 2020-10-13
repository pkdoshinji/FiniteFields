#!/usr/bin/env python3

'''
Python class for computation over a finite field of order p, where
p is prime.

Author: Patrick Kelly
Email: patrickyunen@gmail.com
Last revised: October 13, 2020
'''


import random

class FField:

    def __init__(self, prime, number):
        self.order = prime
        self.value = number
        if self.mr_test(self.order) == False:
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


    def mr_test(self, n, k=40):
    #Miller-Rabin primality test
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        assert (2 ** s * d == n - 1)

        def trial_composite(a):
            if pow(a, d, n) == 1:
                return False
            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    return False
            return True

        for i in range(k):  # number of trials
            a = random.randrange(2, n)
            if trial_composite(a):
                return False

        return True



def main():
    x = FField(65537,31234)
    y = FField(65537,601)

    print(f'x = {x}')
    print(f'y = {y}')
    print('\n')
    print(f'x ** -1 = {x.inverse()}')
    print(f'y ** -1 = {y.inverse()}')
    print('\n')
    print(f'x + y = {x+y}')
    print(f'x - y = {x-y}')
    print(f'x * y = {x*y}')
    print(f'x / y = {x/y}')

if __name__ == '__main__':
    main()

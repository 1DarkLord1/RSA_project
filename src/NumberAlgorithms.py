# coding=utf-8

import random
import math


def fast_pow_mod(number, base, degree):
    res = 1
    while degree:
        if degree % 2:
            res = (res * base) % number
        base = (base * base) % number
        degree //= 2
    return res


def lucas_test(number, primes_decomp, base):
    check = True
    for p in primes_decomp:
        check &= fast_pow_mod(number, base, (number - 1) // p) != 1
    check &= fast_pow_mod(number, base, number - 1) == 1
    return check

def lucas_test_with_python_exp(number, primes_decomp, base):
    check = True
    for p in primes_decomp:
        check &= pow(base, (number - 1) // p, number) != 1
    check &= pow(base, number - 1, number) == 1
    return check


def gen_prime(primes, lower, upper):
    primes_decomp_size = random.randint(4, len(primes))
    primes_decomp = [2] + random.sample(primes, primes_decomp_size)
    max_degree = 40
    number = sum([primes_decomp[i] ** random.randint(1, max_degree) for i in range(primes_decomp_size)]) + 1
    if number < lower or number > upper:
        return None, None, None
    max_base = 128
    for base in range(2, max_base):
        if lucas_test_with_python_exp(number, primes_decomp, base):
            return number, primes_decomp, base
    return None, None, None

def gen_primes():
    lower = 2 ** 123
    upper = 2 ** 128
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
              67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]
    count_iter = 100000
    for i in range(count_iter):
        number, primes_decomp, base = gen_prime(primes, lower, upper)
        if number is not None:
            return number, primes_decomp, base
    return None, None, None

def miller_rabin_test(number, count_iter):
    odd_part = number - 1
    two_degree = 0
    while odd_part % 2 == 0:
        odd_part //= 2
        two_degree += 1
    for i in range(count_iter):
        base = random.randint(1, number - 1)
        cur_degree = fast_pow_mod(number, base, odd_part)
        for j in range(two_degree):
            next_degree = (cur_degree * cur_degree) % number
            if next_degree == 1 and cur_degree != 1 and cur_degree != number - 1:
                return False
            cur_degree = next_degree
        if cur_degree != 1:
            return False
    return True


def gen_pseudoprime():
    lower = 2 ** 123
    upper = 2 ** 128
    count_iter = 100000
    for i in range(count_iter):
        number = random.randint(lower, upper)
        if miller_rabin_test(number, math.ceil(math.log2(number))):
            return number
    return None


def gen_coprime(phi):
    res = random.randint(2, phi - 1)
    while math.gcd(res, phi) != 1:
        res = random.randint(2, phi - 1)
    return res


def gcdex(a, b):
    if a == 0:
        return 0, 1
    x1, y1 = gcdex(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return x, y


def rev(number, modulo):
    rev_elem, y = gcdex(number, modulo)
    rev_elem = (rev_elem % modulo + modulo) % modulo
    return rev_elem


def rsa_gen_keys():
    p = gen_pseudoprime()
    q = gen_pseudoprime()
    if p is None or q is None:
        raise ValueError('Pseudoprime generating error!!!')
    phi = (p - 1) * (q - 1)
    e = gen_coprime(phi)
    d = rev(e, phi)
    return p * q, p, q, e, d


def rsa_encrypt(n, e, t):
    return fast_pow_mod(n, t, e)


def rsa_decrypt(n, d, s):
    return fast_pow_mod(n, s, d)


def prime_factorization_pollard(n, cutoff):
    count_iter = 1000
    factorials = [math.factorial(k) for k in range(1, cutoff)]
    for i in range(count_iter):
        a = gen_coprime(n)
        for k in range(1, cutoff):
            b = (fast_pow_mod(n, a, factorials[k - 1]) + n - 1) % n
            d = math.gcd(b, n)
            if d != 1 and d != n:
                return d
    return 1

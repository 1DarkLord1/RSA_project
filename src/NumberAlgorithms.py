# coding=utf-8
"""Шифрование и дешифрование по RSA.
Проектное домашнее задание по алгебре,
бакалавриат «Современное программирование»
факультета Математики и компьютерных наук СПбГУ"""


def fast_pow_mod(n, a, d):
    res = 1
    while d:
        if d % 2:
            res = (res * a) % n
        a = (a * a) % n
        d //= 2
    return res

def gen_primes():
    """Генерация доказуемо простых на основе теста Люка.

    Возвращает кортеж (n, ps, a), где
    n — простое между 2^123 и 2^128;
    ps — список простых, на которые раскладывается n-1;
    a — число, удовлетворяющее тесту Люка."""
    pass


def gen_pseudoprime():
    """Генерация псевдопростых на основе теста Миллера—Рабина.

    Возвращает целое число n в диапазоне от 2^123 до 2^128,
    псевдопростое по основание не менее чем log(n) чисел."""
    pass


def rsa_gen_keys():
    """Генерация открытого и секретного ключей.

    Возвращает кортеж (n, p, q, e, d), где
    n = p*q;
    p, q — сильно псевдопростые по не менее чем log(q) основаниям;
    e — целое число, меньшее n и взаимно простое с phi(n), значением функции Эйлера от n,
    d — целое число, обратное к e по модулю phi(n)."""
    pass


def rsa_encrypt(n, e, t):
    """Шифрование по RSA.

    На входе открытый ключ n, e и сообщение t.
    Возвращает целое число, равное t^e mod n."""
    pass


def rsa_decrypt(n, d, s):
    """Дешифрование по RSA.

    На входе закрытый ключ n, d и зашифрованное сообщение s.
    Возвращает целое число, равное s^d mod n."""
    pass

def prime_factorization_pollard(n, cutoff):
    """Разложение на простые по алгоритму Полларда.

    На входе целое число n (имеющие вид p*q для некоторых простых p, q)
    и константа отсечения cutoff ~ log(n).
    Возвращает нетривиальный делитель p (или 1, если найти такой не удалось)."""
    pass
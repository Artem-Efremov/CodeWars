"""
If you reverse the word "emirp" you will have the word "prime". That idea is related with the purpose of this kata: we should select all the primes that when reversed are a different prime (so palindromic primes should be discarded).

For example: 13, 17 are prime numbers and the reversed respectively are 31, 71 which are also primes, so 13 and 17 are "emirps". But primes 757, 787, 797 are palindromic primes, meaning that the reversed number is the same as the original, so they are not considered as "emirps" and should be discarded.

The emirps sequence is registered in OEIS as A006567
Your task

Create a function that receives one argument n, as an upper limit, and the return the following array:

[number_of_emirps_below_n, largest_emirp_below_n, sum_of_emirps_below_n]
Examples

find_emirp(10)
[0, 0, 0] ''' no emirps below 10 '''

find_emirp(50)
[4, 37, 98] ''' there are 4 emirps below 50: 13, 17, 31, 37; largest = 37; sum = 98 '''

find_emirp(100)
[8, 97, 418] ''' there are 8 emirps below 100: 13, 17, 31, 37, 71, 73, 79, 97; largest = 97; sum = 418 '''

Happy coding!!

Advise: Do not use a primality test. It will make your code very slow. Create a set of primes using a prime generator or a range of primes producer. Remember that search in a set is faster that in a sorted list or array


"""






def find_emirp(n):
    
    def gen_primes(n):
        limit = 10 ** len(str(n))
        primes = set()
        rev_pr = set()
        more_then_n = set()
        # Sieve of Eratosthenes
        sieve = [True] * (limit)
        for num in range(2, limit):
            if sieve[num]:
                rev = int(str(num)[::-1])
                if rev != num:
                    primes.add(num)
                    rev_pr.add(rev)
                    if rev > n and rev not in more_then_n:
                        more_then_n.add(rev)
                for i in range(num * num, limit, num):
                   sieve[i] = False
        return (primes & rev_pr) - more_then_n


    emirps = gen_primes(n)

    len_emirps, max_emirp, sum_emirps = 0, 0, 0

    for i in emirps:
        len_emirps += 1
        max_emirp = max(i, max_emirp)
        sum_emirps += i

    return [len_emirps, max_emirp, sum_emirps]













def prime_seive(n):
    start = range(n)
    for i1 in start:
        if i1 > 1:
            for i2 in range(i1*2,n,i1):
                start[i2] = 0
    return [i for i in start if i > 1]

def prime(n):
    if n % 2 == 0 or n < 3:return n == 2
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:return False
    return True


def find_emirp(n):
    primes = prime_seive(n)
    emirps = [i for i in primes if prime(int(str(i)[::-1])) and i != int(str(i)[::-1])]
    return [len(emirps),emirps[-1] if len(emirps) > 0 else 0,sum(emirps)]









def find_emirp(n):
    limit = 10 ** len(str(n))
    sieve = [0, 0] + [1] * (limit - 1)
    for i in xrange(int(limit ** .5) + 1):
        if not sieve[i]: continue
        for m in range(i * i, limit + 1, i):
            sieve[m] = 0
    primes = {i for i, b in enumerate(sieve) if b and i != int(str(i)[::-1])}
    semirp = [p for p in xrange(n + 1) if {p, int(str(p)[::-1])} <= primes]
    return [len(semirp), len(semirp) and semirp[-1], sum(semirp)]









def sieve(n):
    isprime = [True for _ in xrange(n+1)]
    for i in xrange(2, int(n ** 0.5) + 1):
        if isprime[i]:
            for j in xrange(i*i, n+1, i):
                isprime[j] = False
    result = []
    for i in xrange(13, n+1):
        if isprime[i]: result.append(i)
    return result
    
primes = set(sieve(10**6))

def is_emirp(p):
    rev = int(str(p)[::-1])
    return p != rev and rev in primes

def find_emirp(n):
    emirps = [p for p in primes if p < n and is_emirp(p)]
    return [len(emirps), max(emirps), sum(emirps)]









from math import log, ceil

def makeSieveEmirp(n):
    sieve, setPrimes = [0]*n, set()
    for i in range(2, n):
        if not sieve[i]:
            setPrimes.add(i)
            for j in range(i**2, n, i): sieve[j] = 1
    return { n for n in setPrimes if n != int(str(n)[::-1]) and int(str(n)[::-1]) in setPrimes }


def find_emirp(n):
    setEmirp = makeSieveEmirp( 10**(int(ceil(log(n,10)))) )
    crunchL = [p for p in setEmirp if p <= n]
    return [len(crunchL), max(crunchL), sum(crunchL)]














def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def find_emirp(n):
    pl = primes(n + 1)[5:]
    if not pl: return [0, 0, 0]
    ps = set(primes(10 ** len(str(n)))[5:])
    lst = [x for x in pl if (str(x) != str(x)[::-1] and int(str(x)[::-1]) in ps)]
    return [len(lst), lst[-1], sum(lst)]










def isprime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 4 == 0:
        return False
    elif n % 5 == 0:
        return False
    for i in range(7, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    sieve = [True] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i*i//2::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

def rev(x):
    return int(str(x)[::-1])

def find_emirp(n):
    a = [p for p in primes(n) if p != rev(p) and isprime(rev(p))]
    return [len(a), max(a) if len(a) > 0 else 0, sum(a)]




































test.describe("Fixed Tests")
nums = [50, 100, 200, 500, 750, 1000] + \
       [3000, 7000, 10000, 15000, 20000] + \
       [50000, 75000, 100000, 120000, 200000, 500000]

results = [[4, 37, 98], [8, 97, 418], [15, 199, 1489], [20, 389, 3232], [25, 743, 6857], [36, 991, 16788]] + \
          [[96, 1979, 103268], [147, 3929, 278175], [240, 9967, 1076242], [446, 14957, 3661772], [627, 19973, 6827225]] + \
          [[980, 39989, 19183366], [1135, 74959, 30404879], [1646, 99989, 76002998], [2205, 119993, 137429553], [4278, 199961, 470781280], [6700, 399941, 1317845448]]

for num, exp in zip(nums, results):
    print("Testing: %s, expecting: %s" % (num, exp))
    test.assert_equals(find_emirp(num), exp)


test.describe("Random Tests")
import random

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

def my_find_emirp(n):
    nStr = str(n)
    maxLim = pow(10, len(nStr))
    primeList = primes2(maxLim)
    primeSet = set(primeList)
    emirps = []
    for prime in primeList:
        if prime > n:
            break
        primeStr = str(prime)
        if primeStr[0] in '2468' or primeStr == primeStr[::-1]:
            continue
        emirp = int(primeStr[::-1])
        if emirp not in primeSet:
            continue
        emirps.append(prime)
    emirps.sort()
    return [len(emirps), emirps[-1], sum(emirps)]

for _ in range(10):
    num = random.randint(500000, 1000000)
    exp = my_find_emirp(num)
    print("Testing: %s, expecting: %s" % (num, exp))
    test.assert_equals(find_emirp(num), exp)

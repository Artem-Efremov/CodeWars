def gen_primes(limit): 
    primes = []
    # Sieve of Eratosthenes
    sieve = [True] * limit
    for num in range(2, limit):
        if sieve[num]:
            primes.append(num)
            for i in range(num * num, limit, num):
               sieve[i] = False
    return primes

print(gen_primes(100000))
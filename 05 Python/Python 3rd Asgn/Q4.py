def isPrime(n):
    is_prime = True

    if n < 2:
        is_prime = False

    for i in range(n-1, 1, -1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def factors(n):
    factors_list = []
    for i in range(1, n+1, 1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list


def primeFactors(n):
    factors_list = factors(n)
    prime_factors = []

    for i in factors_list:
        if isPrime(i):
            prime_factors.append(i)

    return prime_factors


factors_list = factors(42)
prime_factors = primeFactors(42)
print(factors_list)
print(prime_factors)
factors_list = factors(100)
prime_factors = primeFactors(100)
print(factors_list)
print(prime_factors)
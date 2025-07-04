def prime_factors(n):
    factors = []
    divisor = 2
    while n >= 2:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Example usage
number = 56
print(f"Prime factors of {number}: {prime_factors(number)}")
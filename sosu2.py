def prime_factorization(n):
    factors = []
    divisor = 2
    while n >= 2:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

if __name__ == "__main__":
    try:
        num = int(input("素因数分解したい整数を入力してください: "))
        if num < 2:
            print("2以上の整数を入力してください。")
        else:
            print(f"{num} の素因数分解: {prime_factorization(num)}")
    except ValueError:
        print("有効な整数を入力してください。")
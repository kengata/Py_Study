for n in range(1,101):
    if n % 15 == 0:
        print(f"{n}:FizzBuzz")
    elif n % 5 == 0:
        print(f"{n}:Buzz")
    elif n % 3 == 0:
        print(f"{n}:Fizz")
    else:
        continue
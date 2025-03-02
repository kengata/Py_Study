def print_hello():
    print("こんにちは")

print_hello()

def print_hello2(name):
    print(f"{name}さん、こんにちは")

print_hello2("山形")

def add_numbers(a,b):
    c = a + b
    d = a - b
    return c,d

x,y = add_numbers(1,2)
print(x)
print(y)


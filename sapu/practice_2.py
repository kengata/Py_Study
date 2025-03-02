year = 2028

print(year % 4 == 0)
print(year % 100 != 0)
print(year % 400 == 0)

print((year % 4 == 0 and year % 100 != 0))

print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}は閏年です")
else:
    print(f"{year}は閏年ではありません")

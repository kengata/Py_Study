# 集合とタプル

# 集合
# 順序を持たない
x = {0,1,3,6}
y = {0,2,5,6}

# 和集合 0,1,2,3,5,6
z = x | y
print(z)

# 差集合 1,3
z = x - y
print(z)
    
# 積集合 0,6
z = x & y
print(z)

# タプル
# 順序をもつ
x = (1,2,4)
print(x)

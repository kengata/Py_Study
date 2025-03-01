# 配列について

beatles = ['John', 'Paul', 'George', 'Ringo']
rolling_stones = ['Mick', 'Keith', 'Charlie', 'Ronnie']

# loop
for member in beatles:
    print(member)

for member in rolling_stones:
    print(member)

# index
print(f"beatlesの二人目{beatles[1]}")
print(rolling_stones[3])

# length
print(len(beatles))
print(len(rolling_stones))

# append
beatles.append('Pete')
print(beatles)

# remove
beatles.remove('Pete')
print(beatles)

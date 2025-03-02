fruits = ["apple","banana","cherry"]

for fruit in fruits:
   print(fruit)

scores = {"数学": 90, "英語": 70, "理科": 80}
for kamoku,score in scores.items():
   print(f"{kamoku}は{score}点です")

numbers = [10,21,100,18,2]
# range
for x in range(5):
   print(x)

# break
for n in numbers:
   if n >= 100:
      break
   print(f"{n}:繰り返し")
print("loop外")

numbers = [10,21,32,65]
# continue
for n in numbers:
   print(f"{n}:先頭")
   if n % 2 == 0:
      continue    # loopの先頭にもどる
   print(f"{n}:後続")
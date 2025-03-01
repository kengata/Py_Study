# 条件式

nenrei = 51

print(nenrei == 51)
if nenrei == 51:
    print("51歳です")

if nenrei != 51:
    print("51歳ではない")

if nenrei >= 50:
    print("じじい")

if nenrei < 50:
    print("まだまだ")

fruits = ["apple","orange","melon"]
x = "meolon"
if "melon" in fruits:
    print("フルーツにあるよ")

if nenrei >= 51 and "melon" in fruits:
    print("じじいかつメロンあり")

if nenrei >= 20:
    print("おとな")
elif nenrei >=  18:
    print("おとなかつ、酒はまだ")
elif nenrei >= 6:
    print("こどもです")
else:
    print("幼児です")






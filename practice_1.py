scores = {"数学":82,"理科":92,"社会":70,"英語":60,"国語":74}

# 理科と社会の差を求める
diff = scores["理科"] - scores["社会"]
print(f"理科と社会の差は{diff}点です")

# 平均を求める
avg_score = sum(scores.values()) / len(scores)
print(f"avg is {avg_score} 点")

print(type(scores))
print(type(scores.values()))
print(type(scores.keys()))

print(sum(scores.values()))
print(len(scores))
print(len(scores.values()))
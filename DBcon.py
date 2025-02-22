import mysql.connector
import pandas as pd

# mysqlに接続してデータを取得し、CSVファイルに出力するサンプルです。

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'study'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute("SELECT * from meigara_m")
rows = cursor.fetchall()

# カラム名を取得
columns = [desc[0] for desc in cursor.description]

# データフレームに変換
df = pd.DataFrame(rows, columns=columns)

# CSVファイルに出力
df.to_csv('meigara_m.csv', index=False)

# データベースの内容を表示
for row in rows:
    print(row)

cursor.close()
conn.close()

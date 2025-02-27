import mysql.connector
import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv('meigara_m.csv')

# MySQLに接続
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'study'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# データを挿入する
for index, row in df.iterrows():
    cursor.execute("""
    INSERT INTO meigara_m (meigara_cd, meigara_name, tanni, torihiki_teishi, jika)
    VALUES (%s, %s, %s, %s, %s)
    """, tuple(row))

# コミットして接続を閉じる
conn.commit()
cursor.close()
conn.close()

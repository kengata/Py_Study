import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'study'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute("SELECT * from meigara_m where meigara_cd = 9001")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()

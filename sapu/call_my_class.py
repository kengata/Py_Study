# ユーザークラスの生成と更新

# ユーザークラスのインポート
from my_packages.my_class import User

# ユーザー登録（インスタンス生成）
user_1 = User("kei yamagata","keiyama@ex.com",100)
user_2 = User("ken yamagata","ken@gmail",200)

# ポイント更新
user_1.add_point(100)

# ユーザーの表示
print(user_1.name,user_1.mail_address,user_1.point)
print(user_2.name,user_2.mail_address,user_2.point)

# 標準モジュールの理容
# インポート
from datetime import datetime

# datetimeクラスのtodayメソッドの呼び出し
t = datetime.today()
print(t)
class shohin:
    def __init__(self,id,name,price,purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price

    def chg_price(self,price):
        self.price = price

    def chg_purchase_price(self,purchase_price):
        self.purchase_price = purchase_price

    def genka_rate(self):
        genka_rate = self.purchase_price / self.price * 100
        return genka_rate

# 商品登録（クラス生成）
shohin_1 = shohin("A0001","banana",5000,2250)
shohin_2 = shohin("A0002","melon",20000,16000)

# 原価表示（計算メソッドの呼出し）
print(f"{shohin_1.name}の減価率は{shohin_1.genka_rate()}%")
print(f"{shohin_2.name}の減価率は{shohin_2.genka_rate()}%")

# 販売価格の変更（セッタの呼出し）
shohin_1.chg_price(6000)

# 原価表示（価格変更後）（計算メソッドの呼出し）
print(f"{shohin_1.name}の減価率は{shohin_1.genka_rate()}%")
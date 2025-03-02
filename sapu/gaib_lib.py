# 外部ライブラリの利用
# ライブラリのインストール方法
# pipコマンドを使う
#   pipコマンドがない場合はpip3コマンドのシンボリックリンクを作る
#   sudo ln -s /usr/bin/pip3 /usr/local/bin/
# ライブラリのインストール
#   pip install ライブラリ名
#
# pypiのページ
# matplotlib をインストール
# グラフ描画ライブラリ
# pip install matplotlib

import matplotlib.pyplot as plt

# 引数
label = ["A","B","C","D"]
num = [20,17,25,9]

# matplotlibを呼出し
plt.bar(label,num)
plt.savefig('./bar.png')

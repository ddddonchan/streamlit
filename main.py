# streamlit の基本的な操作方法

# import したライブラリの略称を as で指定
import streamlit as st
import numpy as np
import pandas as pd

# titleを追加
st.title('Streamlit 超入門')

# textを追加
# st.write('DataFrame')
# st.write('Display Image')
# st.write('Interactive Widgets')

# -------------------------------------
# 動的なDataFrameを作成
df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# 表示だけならwrite, 引数を指定したい場合はdataframeを使用する
# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0), width=500, height=500)

# 静的な表を表示する
# st.table(df.style.highlight_max(axis=0))

# -------------------------------------
# マジックコマンド
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# -------------------------------------
# チャート(折れ線グラフ)を表示
chr = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b', 'c']
)

# st.line_chart(chr) # 折れ線グラフ
# st.area_chart(chr) # 折れ線グラフの中を塗る
# st.bar_chart(chr) # 棒グラフ

# -------------------------------------
# map
ma = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon'] # lat=緯度, lon=経度
)

# st.map(ma)

# -------------------------------------
# 画像を表示
from PIL import Image

# img = Image.open('IMG_9756.jpeg')
# st.image(img, caption='Momiji', use_column_width=True)

# -------------------------------------
# チェックボックスを表示する、チェックが入っていれば表示
# if st.checkbox('Show Image'):
#     img = Image.open('IMG_9756.jpeg')
#     st.image(img, caption='Momiji', use_column_width=True)

# -------------------------------------
# セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字は？',
#     list(range(1, 11))
# )
# # 'あなたの好きな数字は', option, 'です。' # st.writeを省略することも可能。

# -------------------------------------
# テキスト入力ボックス
# text = st.text_input('あなたの趣味は？') # 複数行入力させたい場合はarea_input
# 'あなたの趣味は', text, 'です。'

# -------------------------------------
# スライダー
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# -------------------------------------
# レイアウトを整える
# サイドバー
# サイドバーに持っていきたいものに st.sideber を付ける
# text = st.sidebar.text_input('あなたの趣味は？')
# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの趣味:', text
# 'コンディション:', condition

# -------------------------------------
# 2カラムレイアウト
# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示') # ボタンを表示

# ボタンが押下されたらテキストを表示
# if button:
#     right_column.write('ここは右カラム')

# -------------------------------------
# エキスパンダー(+ボタンを押すと開く説明画面的なやつ)
# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')

# -------------------------------------
# プログレスバー(ダウンロード中によく見るバー)
import time

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Download {i+1} %')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'
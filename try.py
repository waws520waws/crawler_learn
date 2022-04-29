import pandas as pd
import numpy as np

df = pd.read_csv('./stock_data.csv', encoding='gbk')
# print(df)

df['成交量增减值'] = [i for i in df['成交数量']-df['成交数量'].shift(1)]
print(df)

pos_count = len(df[df['成交量增减值'] > 0])
neg_count = len(df[df['成交量增减值'] < 0])
print('正增长数量：', pos_count)
print('负增长数量：', neg_count)

df['成交量增幅>2%'] = [1 if i > 0.02 else 0 for i in (df['成交数量']-df['成交数量'].shift(1)) / df['成交数量'].shift(1)]
print(df)
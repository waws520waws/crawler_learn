import pandas as pd

df = pd.DataFrame({'usr': ['a', 'a', 'b', 'b', 'a'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': [3, 1, 5, 4, 2],
                   'data2': [13, 11, 15, 14, 12]})

print(df)

'''
需求：
    对于usr中，求出每个usr对应的data1的最大值
        - 法1：可分组排序后取每组中data1的第一个值
        - 法2：直接取每组中data1的最大值
'''

# group_keys=False: 不显示分组键
# lambda x 中的 x 是每一个分组【可 print(x) 查看】
# bb = df.groupby('usr', group_keys=False).apply(lambda x: x.sort_values('data1', ascending=True))
bb = df['data1'].groupby(df['usr']).apply(lambda x: x.sort_values(df['data1'], ascending=True))

print(bb)

# 求每组中data1的均值
aa = df['data1'].groupby(df['usr'], group_keys=False).mean()

print(aa)


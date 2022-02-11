### 1、series 与 dataframe的区别与联系
- 区别
    - series只是一个一维数据结构，它由index和value组成; dataframe是一个二维结构，除了拥有index和value之外，还拥有column
    - Series相当于数组numpy.array类似；DataFrame相当于有表格，有行表头和列表头
    - series的索引名具有唯一性，索引可以是数字和字符；dataframe的索引不具有唯一性，列名也不具有唯一性
- 联系：dataframe由多个series组成，无论是行还是列，单独拆分出来都是一个series

### 2、分组 groupby()
```python
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
bb = df.groupby('usr', group_keys=False).apply(lambda x: x.sort_values('data1', ascending=True))  # 对整个df分组排序，直接写列名
print(bb)

# 求每个usr组中data1的均值
aa = df['data1'].groupby(df['usr'], group_keys=False).mean()

print(aa)
```
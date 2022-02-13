## 1、series 与 dataframe的区别与联系
- 区别
    - series只是一个一维数据结构，它由index和value组成; dataframe是一个二维结构，除了拥有index和value之外，还拥有column
    - Series相当于数组numpy.array类似；DataFrame相当于有表格，有行表头和列表头
    - series的索引名具有唯一性，索引可以是数字和字符；dataframe的索引不具有唯一性，列名也不具有唯一性
- 联系：dataframe由多个series组成，无论是行还是列，单独拆分出来都是一个series

## 2、分组 groupby()
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

## 3、行列操作
## 3.1、 选取行
- 根据某列的值选取行
	
	```
	data1 = df[df['column_name'] == value]
	
	data1 = data[(data.column_name >= t1) & (data.column_name <= t2)]
	```
 
- 按索引选择行
	```
	# 选择idx这一行
	data.loc[[idx]]  # 或者：data.loc[idx:idx] 
	```

- 根据某列的值修改另一列的值
	
	```
	# 示例数据
	data1 = pd.DataFrame([[1, 200011, 33333],
                     [1, 300011, 43333],
                     [2, 40, 5]],
                     columns=['c2', 'time', 'c3'])
	```
	
	```
	data1.loc[:, 'time'] = data1[['time', 'c2']].apply(lambda x: round(x.time/100, 1) if x.c2==1 else x.time, axis=1)
	```

- 按某列最大值选取行
	```
	# 最大值所在行的索引
	idx = data['c3'].idxmax()
	# 某列的最大值
	max_value = data.loc[:, "c3"].max()
	
	# 不管索引是否有顺序，都是选取第一行到此索引所在行(与索引的顺序无关)
	data = data.loc[:idx]  
	```

## 3.2、 选取列
```python
# 按照指定列名选取(data为series类型)
data = df['column_name']
 # 取多列（data为DataFrame类型）
data = df[['column_name1', 'column_name2']] 
 # 按位置取某几列（data为DataFrame类型）
data = df.iloc[:, 0:5] 
```

## 3.3、取指定某行某列的元素
```python
# 取指定第2行第3列的元素
data = df.loc[2][3]
```

### 【注】使用loc、iloc选取数据后的数据类型均保持不变

## 3.4、去重
```
# 去重，并保留第一次重复的值（默认为'first'）
df = df.drop_duplicates(keep='first')

# 去重，不保留重复值
df = df.drop_duplicates(keep=False)

# 根据某些列去重
df = df.drop_duplicates(['col1', 'col3'])
```

## 3.5、某列相邻两个值相减
可以使用shift方法
```
# xx字段向下移动一行的结果，并产生一个新列xx_1，和之前相比向下移动一行，你可以设置为任意行
# 第一行自动用空值填补
df['xx_1'] = df["xx"].shift(1)

# 两列在进行相减，得到差值
df['differ'] = df['xx'] - df["xx_1"]
```

## 3.6、遍历行
```
# 返回索引和每一行
for index, row in df.iterrows():
	print(index, row)
```
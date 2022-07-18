## 1、series 与 dataframe的区别与联系
- 区别
    - series只是一个一维数据结构，它由index和value组成; dataframe是一个二维结构，除了拥有index和value之外，还拥有column
    - Series相当于数组numpy.array类似；DataFrame相当于有表格，有行表头和列表头
    - series的索引名具有唯一性，索引可以是数字和字符；dataframe的索引不具有唯一性，列名也不具有唯一性
    
- 联系：dataframe由多个series组成，无论是行还是列，单独拆分出来都是一个series

    ```python
    print(type(df[['column_name']]))  # DataFrame
    print(type(df['column_name']))  # Series
    ```

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
### 3.1  选取行
- 根据某列的值选取行
	
	```python
	data1 = df[df['column_name'] == value]
	
	data1 = df[df['业务一级分类'].str.contains("金融科技")]
	
	data1 = data[(data.column_name >= t1) & (data.column_name <= t2)]
	
	df.loc[df['column_name'].isin(some_values)]  # some_values是可迭代对象
	
	df.loc[~df['column_name'].isin('some_values')]  # 不等于， ~ 取反
	```
	
- 按索引选择行
	```python
	# 选择idx这一行
	data.loc[[idx]]  # 或者：data.loc[idx:idx] 
	```

- 根据某列的值修改另一列的值
	
	```python
	# 示例数据
	data1 = pd.DataFrame([[1, 200011, 33333],
                     [1, 300011, 43333],
                     [2, 40, 5]],
                     columns=['c2', 'time', 'c3'])
	```
	
	```python
	data1.loc[:, 'time'] = data1[['time', 'c2']].apply(lambda x: round(x.time/100, 1) if x.c2==1 else x.time, axis=1)
	```

- 按某列最大值选取行
	```python
	# 最大值所在行的索引
	idx = data['c3'].idxmax()
	# 某列的最大值
	max_value = data.loc[:, "c3"].max()
	
	# 不管索引是否有顺序，都是选取第一行到此索引所在行(与索引的顺序无关)
	data = data.loc[:idx]  
	```

### 3.2 删除行
- 删除空值行
	```python
	df.dropna(subset=['钱包地址', '银行卡号', '银行卡号归属地', 'image_url'],  # 指定列
			  axis=0,
			  how='all', # how='all'表示若指定列的值都为空，就删掉该行
			  inplace=True)
	```

- 删除某列指定值所在的行

  ```python
  # 使用drop函数以及index参数删除所在的行
  data = df.drop(index=df[(df['卡号'] == '错误') & (df['地址'] == '')].index.tolist())
  
  # 将索引重新排序
  data = data.reset_index(drop=True)
  ```
  
  

### 3.2 列操作

- 选取列

```python
# 按照指定列名选取(data为series类型)
data = df['column_name']
 # 取多列（data为DataFrame类型）
data = df[['column_name1', 'column_name2']] 
 # 按位置取某几列（data为DataFrame类型）
data = df.iloc[:, 0:5] 
```

- 调整列的位置（或顺序）

```python
df = pd.DataFrame({'a': [1, 2, 3],
                   'b': [4, 5, 6],
                   'c': [7, 8, 9]})

new_columns = ['c', 'b', 'a']
df = df.reindex(columns=new_columns)
```



### 3.3 取指定某行某列的元素

```python
# 取指定第2行第3列的元素
data = df.loc[2][3]
```

**【注】使用loc、iloc选取数据后的数据类型均保持不变**

### 3.4 去重
```python
# 去重，并保留第一次重复的值（默认为'first'）
df = df.drop_duplicates(keep='first')

# 去重，不保留重复值
df = df.drop_duplicates(keep=False)

# 根据某些列去重
df = df.drop_duplicates(['col1', 'col3'])
```

### 3.5 某列相邻两个值相减
可以使用shift方法
```python
# xx字段向下移动一行的结果，并产生一个新列xx_1，和之前相比向下移动一行，你可以设置为任意行
# 第一行自动用空值填补
df['xx_1'] = df["xx"].shift(1)

# 两列在进行相减，得到差值
df['differ'] = df['xx'] - df["xx_1"]
```

### 3.6 遍历行
```python
# 返回索引和每一行
for index, row in df.iterrows():
	print(index, row)
```

### 3.7  处理列并添加为新列（apply）

```python
def handle(website):
    if website.startswith('http'):
        return website.split('/')[2]
    else:
        return website
df['handled_website'] = df[['official_website']].apply(lambda x: handle(x.official_website), axis=1)
df['sex_not_male'] = df[['sex']].apply(lambda x: 1 if x.sex != '女' else 0, axis=1)

```
```python
def extract_info(content):
	# 一系列操作
	payee = ''
	payment_account = ''
	payment_bank = ''
	
	return payee, payment_account, payment_bank

# 使用 result_type="expand" 返回多列，并赋值
df[['收款人', '收款账号', '收款银行']] = df[['content']].apply(lambda x: extract_info(x.content), axis=1, result_type="expand")
```


## 4、读取/存入数据库

```python
import pandas as pd
from sqlalchemy import create_engine, types
import pymysql
pymysql.install_as_MySQLdb()  # 必须

# 简易写法
# df = pd.read_sql_table('table_name', "mysql://root:12345678@192.168.224.49:33060/database_name")

engine = create_engine("mysql://root:12345678@192.168.224.49:33060/database_name", echo=True)
conn = engine.connect()

## 读
df = pd.read_sql_table('table_name', conn)

## 存
# 若数据库中没有这个表，会自动创建；若存在，则根据if_exists来操作，同时也会改变表结构
# if_exists: 当数据库中已经存在数据表时对数据表的操作，有replace替换、append追加、fail当表存在时提示ValueError
# dtype: 其中可以指定某列的数据类型，设置主键等操作
df.to_sql('table_name', con=conn, if_exists='replace', index=False, dtype={'col_name': types.VARCHAR(20)})
conn.close()

# 也可以执行sql语句
with engine.connect() as con:
    con.execute("""ALTER TABLE `{}`.`{}` \
            ADD COLUMN `id` INT NOT NULL AUTO_INCREMENT FIRST, \
            ADD PRIMARY KEY (`id`);"""
                .format(db_name, table_name))

sql = "select `消息内容` from `ok钱包2_历史对话_224377` where `消息内容` regexp '^http.*?(jpg|png)$'"
results = conn.execute(sql)
for result in results:
	print(result)
```

## 5、excel操作

```python
import pandas as pd

## 读
df = pd.read_excel('./icon2_data/token_detail1.xlsx', sheet_name='sheet1')

## 写
# 防止将 url 存储为超链接（若为超链接，打开xlsx会报错）
writer = pd.ExcelWriter('xxxx.xlsx', engine='xlsxwriter', engine_kwargs={'options': {'strings_to_urls': False}})
df.to_excel(writer, index=False)
writer.close()
```

## 5、pycharm中显示 df 所有列/行
```python
import pandas as pd 
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
```

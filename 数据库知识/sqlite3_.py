import sqlite3

conn = None


# 创建表
def create():
    global conn

    '''
    - 参数1: db_name，数据库名称
    - 参数2: timeout=3，指当一个数据库被多个连接访问，且其中一个修改了数据库，此时 SQLite 数据库被锁定，直到事务提交。
            timeout 参数表示连接等待锁定的持续时间，直到发生异常断开连接。timeout 参数默认是 5.0（5 秒）。
    - 参数3: isolation_level=None，事务隔离级别，设置为None即自动提交，即每次写数据库都提交。
            不需要自动提交时只需去掉isolation_level参数，通过 conn.commit() 提交事务。
    - 参数4: check_same_thread=False，允许在其他线程中使用这个连接 。
    '''
    conn = sqlite3.connect('mysqlite.db', timeout=3, isolation_level=None, check_same_thread=False)

    conn.execute(
        """
        create table if not exists bilibili_users(
            id int prinmary key autocrement,
            mid varchar DEFAULT NULL,
            name varchar DEFAULT NULL,
            follow int DEFAULT NULL,
            fans int DEFAULT NULL,
            black int DEFAULT NULL,
            lv int DEFAULT NULL)
        """
    )


# 插入数据
def save(result=()):
    # 将数据保存至本地
    global conn
    if result == ():
        return
    command = "insert into bilibili_users values(?,?,?,?,?,?,?);"
    try:
        conn.execute(command, result)
    except Exception as e:
        print("save wrong")
        print(e)
        conn.rollback()
    conn.commit()


# 读取数据
conn = sqlite3.connect('users.db')
c = conn.cursor()
print("Opened database successfully")
cursor = c.execute("SELECT *  from bilibili_users")
for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2] + "\n")

conn.close()

import sqlite3
# 全局变量conn
conn = None
# 创建一个数据库
def create():
    global conn
    # 注意这个地方设置的参数，参见下述说明
    conn = sqlite3.connect('users.db', timeout=3,
                           isolation_level=None, check_same_thread=False)
    conn.execute("""
    create table if not exists bilibili_users(
    id int prinmary key autocrement ,
    mid varchar DEFAULT NULL,
    name varchar DEFAULT NULL,
    follow int DEFAULT NULL,
    fans int DEFAULT NULL,
    black int DEFAULT NULL,
    lv int DEFAULT NULL)""")
if __name__ == "__main__":
    create()

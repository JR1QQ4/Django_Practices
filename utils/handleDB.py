import sqlite3


conn = sqlite3.connect('../db.sqlite')
c = conn.cursor()

# 创建表
# c.execute('''CREATE TABLE USERS(
#     ID    INTEGER PRIMARY KEY    AUTOINCREMENT,
#     NAME    varchar    NOT NULL,
#     PASSWORD    varchar    NOT NULL,
#     EMAIL    varchar);''')
# conn.commit()

# 插入数据
# c.execute("INSERT INTO USERS (ID,NAME,PASSWORD,EMAIL) \
#       VALUES (1, 'Admin', '123456', 'admin@admin.com' )")
# c.execute("INSERT INTO USERS (NAME,PASSWORD,EMAIL) \
#       VALUES ('mc', '123456', 'admin@admin.com' )")
# conn.commit()

# 查询
cursor = c.execute("SELECT id, name, PASSWORD, EMAIL  from USERS")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("PASSWORD = ", row[2])
   print("EMAIL = ", row[3])

# 更新
# c.execute("UPDATE USERS set EMAIL='mc@mc.com'  where ID=2")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)

# 删除
# c.execute("DELETE from USERS where ID=2;")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)

conn.close()

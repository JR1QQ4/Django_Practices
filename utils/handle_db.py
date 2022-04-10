import sqlite3

import os

from handle_path import project_path


class SiteDB:
    _conn = None
    _c = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            obj = super(SiteDB, cls)
            cls._instance = obj.__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if self._conn is None:
            self._conn = sqlite3.connect(os.path.join(project_path, 'db.sqlite3'))
            self._c = self._conn.cursor()

            try:
                self.execute("SELECT * FROM USERS")
            except Exception as e:
                # 创建表
                self._c.execute('''CREATE TABLE USERS(
                    ID    INTEGER PRIMARY KEY    AUTOINCREMENT,
                    NAME    varchar    NOT NULL,
                    PASSWORD    varchar    NOT NULL,
                    EMAIL    varchar);''')

                # 插入数据
                self._c.execute("INSERT INTO USERS (ID,NAME,PASSWORD,EMAIL) \
                    VALUES (1, 'Admin', '123456', 'admin@admin.com' )")
                self._c.execute("INSERT INTO USERS (NAME,PASSWORD,EMAIL) \
                    VALUES ('mc', '123456', 'admin@admin.com' )")

            # 提交
            self._conn.commit()

    def close(self):
        self._conn.close()
        self._conn = None

    def execute(self, sql_str):
        res = self._c.execute(sql_str)
        self._conn.commit()
        return res

# 查询
# cursor = c.execute("SELECT id, name, PASSWORD, EMAIL  from USERS")
# for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("PASSWORD = ", row[2])
#    print("EMAIL = ", row[3])

# 更新
# c.execute("UPDATE USERS set EMAIL='mc@mc.com'  where ID=2")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)

# 删除
# c.execute("DELETE from USERS where ID=2;")
# conn.commit()
# print("Total number of rows updated :", conn.total_changes)

# if __name__ == '__main__':
#     site_db_0 = SiteDB()
#     cursor = site_db_0.execute("SELECT id, name, PASSWORD, EMAIL  from USERS")
#     for row in cursor:
#        print("ID = ", row[0])
#        print("NAME = ", row[1])
#        print("PASSWORD = ", row[2])
#        print("EMAIL = ", row[3])

#     site_db_1 = SiteDB()

#     print(id(site_db_0))
#     print(id(site_db_1))

#-*- coding:utf-8 -*-

import sqlite3

class DBOption():
    def __init__(self, db_path='db.sqlite'):
        self.conn = sqlite3.connect(db_path)
        self.conn.isolation_level = None
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def query_data(self, query_sql):
        """
        数据查询方法
        :param query_sql 查询语言
        """

        self.cur.execute(query_sql)
        return [item for item in self.cur.fetchall()]

    def insert_data(self, insert_many_sql, data):
        """
        批量插入数据
        """
        try:
            self.cur.executemany(insert_many_sql, data)
            self.conn.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def insert_data_by_script(self, insert_script):
        """
        以SQLinsert语句的方式插入
        """
        try:
            self.conn.executescript(insert_script)
            return True
        except Exception as err:
            print(err)
            return False

    def close(self):
        self.cur.close()
        self.conn.close()

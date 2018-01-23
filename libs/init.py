#-*- coding:utf-8 -*-
"""
工程初始化，插入初始化数据
"""
import json
from DB import DBOption


db_option = DBOption('db.sqlite')

def load_json_data(json_file_path="config.json"):

    config = []
    with open(json_file_path, 'r') as fp:
        for line in fp.readlines():
            config.append(line)

    return json.loads(''.join(config))



def init_airline_db_data():
    """
    初始化航空公司数
    """

    airline_data = []
    for item in load_json_data()['airline']:
        airline_data.append((item['id'], item['code'], item['name'], item['url']))

    insert_many_sql = "INSERT INTO airline VALUES (?, ?, ?, ?)"

    result = db_option.insert_data(insert_many_sql, airline_data)
    print(result)
    db_option.close()


def main():
    init_airline_db_data()


if __name__ == '__main__':
    main()
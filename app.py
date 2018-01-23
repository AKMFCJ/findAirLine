#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/22
"""
爬虫启动入口
出发地/目的地/出发日期
"""
import sys
import argparse
from datetime import datetime
from libs.DB import DBOption
from airlineSpider.ceair import ceair_fligth

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Airline spider")
parser.add_argument('-o', '--orgCity', action="store", dest="org_city", default='ngk',  help='出发城市')
parser.add_argument('-d', '--dstCity', action="store", dest="dst_city", help='目的城市')
parser.add_argument('-f','--flightDate', action="store", dest="fligth_date", help='出发日期格式是2018-01-02')


def main():
    args = parser.parse_args()
    org_city =  args.org_city
    dst_city = args.dst_city
    fligth_date = args.fligth_date
    if not fligth_date:
        fligth_date = datetime.now().strftime('%Y-%m-%d')
    print org_city, dst_city, fligth_date
    db_option = DBOption('libs/db.sqlite')
    org_city_code_query = "SELECT code FROM city WHERE name IN('%s')" % org_city
    dst_city_code_query = "SELECT code FROM city WHERE name IN('%s')" % dst_city
    org_city_code = db_option.query_data(org_city_code_query)[0][0].lower()
    dst_city_code = db_option.query_data(dst_city_code_query)[0][0].lower()

    fligth_count_sql = "SELECT COUNT(id) FROM flight"
    flight_count = db_option.query_data(fligth_count_sql)[0][0]
    flight_count += 1

    # 东方航空
    fligth_info =  ceair_fligth(org_city_code, dst_city_code, datetime.strptime(fligth_date, '%Y-%m-%d').strftime('%y%m%d')).split(' ')
    flight_date = []
    ceair_fligth_info = [(flight_count, fligth_info[1][:-1],org_city,dst_city, fligth_info[2], str(fligth_date), str(fligth_date),'',fligth_info[-1], ' '.join(fligth_info))]
    fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    db_option.insert_data(fligth_insert_sql, ceair_fligth_info)
    db_option.close()
    


if __name__ == '__main__':
    main()
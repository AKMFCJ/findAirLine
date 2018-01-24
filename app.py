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
from airlineSpider.ceair import ceair_flight
from airlineSpider.csair import csair_flight
from airlineSpider.xiamenair import xiamenair_flight
from airlineSpider.jdair import jdair_flight
from airlineSpider.juneyaoair import juneyaoair_flight


reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Airline spider")
parser.add_argument('-o', '--orgCity', action="store", dest="org_city", default='ngk',  help='出发城市')
parser.add_argument('-d', '--dstCity', action="store", dest="dst_city", help='目的城市')
parser.add_argument('-f','--flightDate', action="store", dest="flight_date", help='出发日期格式是2018-01-02')


def main():
    args = parser.parse_args()
    org_city =  args.org_city
    dst_city = args.dst_city
    flight_date = args.flight_date
    if flight_date:
        try:
            datetime.strptime(flight_date, '%Y-%m-%d')
        except Exception as err:
            print err
            print u'日期格式不正确,格式参考2018-01-02'
            sys.exit(1)
    else:
        fligth_date = datetime.now().strftime('%Y-%m-%d')

    print org_city, dst_city, flight_date

    db_option = DBOption('libs/db.sqlite')
    org_city_code_query = "SELECT code FROM city WHERE name IN('%s')" % org_city
    dst_city_code_query = "SELECT code FROM city WHERE name IN('%s')" % dst_city
    org_city_code = db_option.query_data(org_city_code_query)[0][0]
    dst_city_code = db_option.query_data(dst_city_code_query)[0][0]

    fligth_count_sql = "SELECT COUNT(id) FROM flight"
    flight_count = db_option.query_data(fligth_count_sql)[0][0]
    flight_count += 1

    # 东方航空
    flight_info, price =  ceair_flight(org_city_code.lower(), dst_city_code.lower(), datetime.strptime(flight_date, '%Y-%m-%d').strftime('%y%m%d'))
    if flight_info:
        flight_info = flight_info.split(' ')
        ceair_fligth_info = [(flight_count, flight_info[1][:-1],org_city,dst_city, flight_info[2], str(flight_date), str(flight_date), '', price, ' '.join(flight_info))]
        fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_option.insert_data(fligth_insert_sql, ceair_fligth_info)
        flight_count += 1

    # 南方航空
    flight_name, flight_info, price = csair_flight(org_city_code, dst_city_code, flight_date)
    if flight_info:
        flight_info = flight_info.split('\n')
        if flight_info[2].strip().startswith('CZ'):
            flight_name = flight_info[2].strip()
        csair_fligth_info = [(flight_count, flight_name, org_city, dst_city, flight_info[2], str(flight_date),
                              str(flight_date), '', price, ' '.join(flight_info))]
        fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_option.insert_data(fligth_insert_sql, csair_fligth_info)
        flight_count += 1

    # 厦门航空
    flight_name, flight_info, price = xiamenair_flight(org_city_code, dst_city_code, flight_date)
    if flight_info:
        flight_info = flight_info.split('\n')
        xiamenair_fligth_info = [(flight_count, flight_name, org_city, dst_city, flight_info[2], str(flight_date),
                              str(flight_date), '', price, ' '.join(flight_info))]
        fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_option.insert_data(fligth_insert_sql, xiamenair_fligth_info)
        flight_count += 1

    # 首都航空
    flight_name, flight_info, price = jdair_flight(org_city_code, dst_city_code, flight_date)
    if flight_info:
        flight_info = flight_info.split('\n')
        xiamenair_fligth_info = [(flight_count, flight_name, org_city, dst_city, flight_info[2], str(flight_date),
                              str(flight_date), '', price, ' '.join(flight_info))]
        fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_option.insert_data(fligth_insert_sql, xiamenair_fligth_info)
        flight_count += 1

    # 吉祥航空
    flight_name, flight_info, price = juneyaoair_flight(org_city, org_city_code, dst_city, dst_city_code, flight_date)
    if flight_info:
        flight_info = flight_info.split('\n')
        xiamenair_fligth_info = [(flight_count, flight_name, org_city, dst_city, flight_info[2], str(flight_date),
                              str(flight_date), '', price, ' '.join(flight_info))]
        fligth_insert_sql = "INSERT INTO flight (id, name, org_city, dst_city, category, start_date, end_date, duration, price, detail_info) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db_option.insert_data(fligth_insert_sql, xiamenair_fligth_info)
        flight_count += 1

    db_option.close()



if __name__ == '__main__':
    main()
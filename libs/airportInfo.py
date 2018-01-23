#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/23
"""
从中国民航网站爬取国内机场名称和代码
http://www.carnoc.com/mhzl/jchzl/airport3code.htm
"""
from selenium import webdriver
from DB import DBOption


airport_url = 'http://www.carnoc.com/mhzl/jchzl/airport3code.htm'

browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
browser.implicitly_wait(20)
browser.get(airport_url)

tr_list = browser.find_elements_by_xpath('//tbody/tr')
is_data = False

city_data = []
for item in tr_list:
    if item.text.startswith(u'阿勒泰'):
        is_data = True
    if item.text.startswith(u'关于CARNOC'):
        is_data = False
    if is_data:
        city_data.append([city.strip() for city in  item.text.split(' ') if city.strip()])

city_list = []
db_id = 1
for item in city_data:
    for index in range(0, len(item), 2):
        city_info = item[index: index+2]
        city_info.insert(0, db_id)
        city_list.append(tuple(city_info))
        db_id += 1

db_option = DBOption()
insert_many_sql = "INSERT INTO city (id, name, code) VALUES(?, ?, ?)"
db_option.insert_data(insert_many_sql, city_list)
db_option.close()

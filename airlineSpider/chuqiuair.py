#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/24
"""
春秋航空公司https://flights.ch.com/SHA-KMG.html?Departure={0}&Arrival={1}&FDate={2}&RetDate={3}&ANum=1&CNum=0&INum=0&MType=0&IfRet=false&SType=01&IsEmployee=false&isBg=false&IsJC=false
"""


import re
# import sys
from selenium import webdriver

# reload(sys)
# sys.setdefaultencoding('utf-8')


def chuqiuair_flight(org_city_code, dst_city_code, org_city, dst_city, flight_date):
    airline_url = 'https://flights.ch.com/{0}-{1}.html?Departure={2}&Arrival={3}&FDate={4}&RetDate={5}&ANum=1&CNum=0&INum=0&MType=0&IfRet=false&SType=01&IsEmployee=false&isBg=false&IsJC=false'.format(org_city_code, dst_city_code, org_city, dst_city, flight_date, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)

    try:
        flight_list = browser.find_elements_by_xpath('//div[@class="flight-block"]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return '', '', ''

    cheapest_flight = None
    cheapest_price = ''
    for item in flight_list:
        price_item = item.find_element_by_xpath('//span[@class="currency"]')
        if price_item:
            cheapest_flight = item
            cheapest_price = price_item.text
            cheapest_price = re.findall("\d+", cheapest_price)[0]
            break

    if cheapest_flight:
        cheapest_flight_text = cheapest_flight.text
        browser.quit()
        return ''.join(['9C', cheapest_flight_text.split('\n')[0].split('9C')[1]]), cheapest_flight_text, cheapest_price
    browser.quit()
    return '', '', ''


# print chuqiuair_flight('SHA', 'SYX', '上海', '三亚', '2018-03-03')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/24
"""
厦门航空机票接口
https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo={0},{1},{2}
"""
# import sys
from selenium import webdriver

# reload(sys)
# sys.setdefaultencoding('utf-8')


def xiamenair_flight(org_city, dst_city, flight_date):
    airline_url = 'https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo={0},{1},{2}'.format(org_city, dst_city, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)

    try:
        flight_list = browser.find_elements_by_xpath('//div[@class="form-mess-inner segment-info bor-d1-bd"]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return '', '', ''

    cheapest_flight = None
    cheapest_price = ''
    for item in flight_list:
        price_item = item.find_elements_by_class_name('flight-price')
        if price_item:
            price = price_item[0].text.split('￥')[1]
            if not cheapest_flight and not cheapest_price:
                cheapest_flight = item
                cheapest_price = price

            if price and int(cheapest_price) > int(price):
                cheapest_flight = item
                cheapest_price = price

    if cheapest_flight:
        cheapest_flight_text = cheapest_flight.text
        browser.quit()
        return cheapest_flight_text.split('\n')[0], cheapest_flight_text, cheapest_price
    browser.quit()
    return '', '', ''


# print xiamenair_fligth('NKG', 'XMN', '2018-03-03')
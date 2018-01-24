#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/24
"""
首都航空公司
http://www.jdair.net/b2c-flight/searchflight.action?&tripType=OW&orgCity={0}&dstCity={1}&flightDate={2}&returnDate=
"""
# import sys
from selenium import webdriver

# reload(sys)
# sys.setdefaultencoding('utf-8')


def jdair_flight(org_city, dst_city, flight_date):
    airline_url = 'http://www.jdair.net/b2c-flight/searchflight.action?&tripType=OW&orgCity={0}&dstCity={1}&flightDate={2}&returnDate='.format(org_city, dst_city, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)

    try:
        flight_list = browser.find_elements_by_xpath('//div[@class="flightInfo "]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return '', '', ''

    cheapest_flight = None
    cheapest_price = ''
    for item in flight_list:
        price_item = item.find_element_by_xpath('//span[@class="f_30_rb "]')
        if price_item:
            cheapest_flight = item
            cheapest_price = price_item.text
            break

    if cheapest_flight:
        cheapest_flight_text = cheapest_flight.text
        browser.quit()
        return cheapest_flight_text.split('\n')[0], cheapest_flight_text, cheapest_price
    browser.quit()
    return '', '', ''


# print jdair_fligth('NKG', 'LJG', '2018-03-03')
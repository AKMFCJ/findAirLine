#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/24
"""
吉祥航空http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW&sendCity={0}&sendCode={1}&arrCity={2}&arrCode={3}&directType=N&tripType=D&departureDate={4}&returnDate={4}
"""


import re
# import sys
from selenium import webdriver

# reload(sys)
# sys.setdefaultencoding('utf-8')


def juneyaoair_flight(org_city, org_city_code, dst_city, dst_city_code, flight_date):
    airline_url = 'http://www.juneyaoair.com/pages/Flight/flight.aspx?flightType=OW&sendCity={0}&sendCode={1}&arrCity={2}&arrCode={3}&directType=N&tripType=D&departureDate={4}&returnDate={4}'.format(org_city, org_city_code, dst_city, dst_city_code, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)

    try:
        flight_list = browser.find_elements_by_xpath('//tr[@class="title"]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return '', '', ''

    cheapest_flight = None
    cheapest_price = ''
    for item in flight_list:
        price_item = item.find_element_by_xpath('//div[@class="flt_price"]')
        if price_item:
            cheapest_flight = item
            cheapest_price = price_item.text
            cheapest_price = re.findall("\d+", cheapest_price)[0]
            break

    if cheapest_flight:
        cheapest_flight_text = cheapest_flight.text
        browser.quit()
        return cheapest_flight_text.split('\n')[0], cheapest_flight_text, cheapest_price
    browser.quit()
    return '', '', ''


# print juneyaoair_flight('南京', 'NKG', '三亚', 'SYX', '2018-03-03')
# print juneyaoair_flight('南京', 'NKG', '丽江', 'LJG', '2018-03-03')
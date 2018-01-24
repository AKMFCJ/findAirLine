#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by AKM_FAN@163.com on 2018/1/23
"""
海南航空机票爬虫
http://new.hnair.com/hainanair/ibe/common/flightSearch.do
"""
import sys
import requests
from selenium import webdriver


reload(sys)
sys.setdefaultencoding('utf-8')


def hnair_fligth(org_city, dst_city, flight_date):
    """

    @param org_city: 出发城市编码
    @param dst_city: 到达城市编码
    @param flight_date: 航班日期
    @return:
    """
    airline_url = 'http://new.hnair.com/hainanair/ibe/common/flightSearch.do'
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)
    browser.execute_script("$('#Search-OriginDestinationInformation-Origin-location').value = 'CITY_SYX_CN';"
                           "$('#Search-OriginDestinationInformation-Origin-location_input_location').value = '三亚';"
                           "$('#Search-OriginDestinationInformation-Destination-location').value = 'CITY_NKG_CN';"
                           "$('#Search-OriginDestinationInformation-Destination-location_input_location').value = '南京';")
    browser.find_element_by_xpath('//a[@class="class="button-red-short btn-confirm btn-vali"]').click()
    print browser.current_url

    # print browser.get_cookies()
    # # browser.execute_script("return $('#Search-OriginDestinationInformation-Origin-location').value = 'CITY_NKG_CN';")
    # org_city_input = browser.find_element_by_id('Search-OriginDestinationInformation-Origin-location')
    # print org_city_input
    # print(dir(org_city_input))
    # org_city_input.clear()
    # org_city_input.send_keys('CITY_NKG_CN')
    # dst_city_input = browser.find_element_by_id('Search-OriginDestinationInformation-Destination-location')
    # dst_city.clear()
    # dst_city.send_keys('CITY_SYX_CN')
    # flight_date_input = browser.find_element_by_name('Search/DateInformation/departDate_display')
    # flight_date_input.clear()
    # flight_date_input.send_keys(flight_date)



    # print org_city_input.get_attribute('value')
    # print dst_city_input.get_attribute('value')
    # print flight_date_input.get_attribute('value')
    # print search_button
    # print browser.current_url

    # headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Accept-Encoding": "gzip, deflate",
    #     "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,la;q=0.6",
    #     "Cache-Control": "max-age=0",
    #     "Connection": "keep-alive",
    #     "Content-Length": "936",
    #     "Content-Type": "application/x-www-form-urlencoded",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    # }
    # airline_url = 'http://new.hnair.com/hainanair/ibe/common/processSearchForm.do'
    # playload = {
    #     "Search / AirlineMode": "false",
    #     "Search / calendarCacheSearchDays": "60",
    #     "Search / calendarSearched": "false",
    #     "dropOffLocationRequired": "false",
    #     "Search / searchType": "F",
    #     "searchTypeValidator": "F",
    #     "xSellMode": "false",
    #     "Search / flightType": "oneway",
    #     "destinationLocationSearchBoxType": "L",
    #     "Search / OriginDestinationInformation / Origin / location": "CITY_NKG_CN",
    #     "Search / OriginDestinationInformation / Origin / location_input": "南京",
    #     "Search / OriginDestinationInformation / Destination / location": "CITY_SYX_CN",
    #     "Search / OriginDestinationInformation / Destination / location_input": "三亚",
    #     "Search / DateInformation / departDate_display": "2018 - 02 - 28",
    #     "Search / DateInformation / departDate": "2018 - 02 - 28",
    #     "Search / DateInformation / returnDate": "2018 - 03 - 02",
    #     "Search / seatClass": "Y",
    #     "Search / calendarSearch": "false",
    #     "Search / Passengers / adults": "1",
    #     "Search / Passengers / children": "0",
    #     "Search / Passengers / MilitaryDisabled": "0",
    #     "Search / Passengers / PoliceDisabled": "0",
    #     "Search / promotionCode": ""
    #
    # }
    # response = requests.post(airline_url, headers=headers, data=playload)
    # for item in  response.text.split('\n'):
    #     if item.strip().startswith('document.waitingForm.action'):
    #         print ''.join(item.split(' '))


hnair_fligth(u'南京', u'三亚', '2018-02-28')
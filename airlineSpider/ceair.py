#-*- coding:utf-8 -*-
'''
东方航空公司机票价格接口
'''

from selenium import webdriver


def ceair_flight(org_city, dst_city, flight_date):
    airline_url = 'http://www.ceair.com/booking/{0}-{1}-{2}_CNY.html'.format(org_city, dst_city, flight_date)
    print(airline_url)

    browser = webdriver.Chrome('/Users/roy/Downloads/tmp/chromedriver')
    browser.implicitly_wait(20)
    browser.get(airline_url)
    # from_city = browser.find_element_by_xpath('//input[@class="input big city _display"]')
    # flight_list = browser.find_elements_by_css_selector("ul.basic-info")

    try:
        flight_list = browser.find_elements_by_xpath('//ul[@class="basic-info"]')
    except Exception as err:
        browser.quit()
        print err
        print u'没有%s当日的航班信息' % flight_date
        return ''

    cheapest_price = ''
    fligth_info = []
    for item in flight_list[0].text.split('\n'):
        if item.strip():
            fligth_info.append(item.strip())

    if fligth_info[-1].startswith('— —'):
        if fligth_info[-2].startswith('— —'):
            cheapest_price = fligth_info[-3]
        else:
            cheapest_price = fligth_info[-2]
    else:
        cheapest_price = fligth_info[-1]

    if not cheapest_price.find('— —') >= 0:
        cheapest_price = cheapest_price.split(' ')[1].replace(',', '')

    browser.quit()
    return ''.join(fligth_info), cheapest_price

from django.core.management.base import BaseCommand, CommandError
import time, re, datetime, os
from selenium import webdriver
from crawler.models import notice


class Command(BaseCommand):

    def handle(self, *args, **options):

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver'), options=options)

        url = "http://hansei.sen.hs.kr/50646/subMenu.do"

        # 학교 홈페이지 접속
        driver.get(url)
        time.sleep(3)

        listG = ['1','2','3','4','5','6','7','8','9','10']

        for i in listG:

            xpath_G = '//*[@id="board_area"]/table/tbody/tr['+i+']/td[2]/a'
            driver.find_element_by_xpath(xpath_G).click()

            writer = driver.find_element_by_xpath('''//*[@id="board_area"]/table/tbody/tr[1]/td[1]/div''').text
            date = driver.find_element_by_xpath('''//*[@id="board_area"]/table/tbody/tr[1]/td[2]/div''').text
            title = driver.find_element_by_xpath('''//*[@id="board_area"]/table/tbody/tr[2]/td/div''').text
            detail = driver.find_element_by_xpath('''//*[@id="board_area"]/table/tbody/tr[3]/td/div''').text

            date = datetime.datetime.strptime(date, '%Y-%m-%d')

            driver.find_element_by_xpath('//*[@id="sub_navigation_320677"]/div/ul/li[2]/a').click()
            time.sleep(1)

            try:
                notice(writer=writer, date=date, title=title, detail=detail).save()

            except:
                continue

        driver.close()

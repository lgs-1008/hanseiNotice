from django.core.management.base import BaseCommand, CommandError
import time, re, datetime, os
from selenium import webdriver

from crawler.models import notice


class Command(BaseCommand):

    def handle(self, *args, **options):
        # User Agent 설정
        options = webdriver.ChromeOptions()
        #options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        # driver 인스턴스 생성
        #driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe'), options=options)

        #브라우저가 열리지 않게 헤드리스로 작동하게끔 해주는 코드.
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")

        #driver = webdriver.Chrome('./chromedriver.exe')
        driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver'), options=options)

        url = "http://hansei.sen.hs.kr/50646/subMenu.do"

        # 나이스 접속
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
            #print("공지시작 --------------------------------------------")
            #print(writer)
            #print(date)
            #print(title)
            #print(detail)
            #print("공지끝 ----------------------------------------------")



        driver.close()

"""
author: 王璐斯
file: 腾讯课堂.py
time: 2022/10/20 11:21
"""
from selenium import webdriver
import csv, time

url = 'https://ke.qq.com/course/list?mt=1001&st=2064&page=1'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless--')
chrome_options.add_argument('--disable-gpu')
chrome_options.headless = True
bro = webdriver.Chrome(options=chrome_options)
bro.get(url)
with open('timi.csv', 'a+', encoding='utf-8', newline='')as f:
    love = csv.writer(f)
    love.writerow(['课程名字', '课程链接'])
    for i in range(34):
        section = bro.find_elements_by_xpath('//div[@class="course-list"]/div')
        for base in section:
            links = base.find_element_by_xpath('.//section/a')
            link = links.get_attribute('href')
            names = base.find_element_by_xpath('.//section/a/div/h3').text
            print(link, names)
            love.writerow([names, link])
        cat = bro.find_element_by_xpath('//ul/li[@title="下一页"]')
        cat.click()
        time.sleep(1)
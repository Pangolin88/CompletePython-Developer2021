from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import pprint


driver = webdriver.Chrome()
_cookie = { "name": "MoodleSession", "value": "qob1hspcah8dsav7qeqdkl1be2" }
driver.get("http://homework.topicanative.edu.vn/local/lemanager/detail.php?id=523")
driver.add_cookie(_cookie)
username = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[3]/form/div/div[3]/div[1]/input')
username.send_keys('huynhviha1703@gmail.com')
pwd = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[3]/form/div/div[3]/div[2]/input')
pwd.send_keys('UnuSU3AFY6ji6y6')

driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[3]/form/input').click()

def get_transcript(a_elements):
    transcript1 = ''
    transcript2 = ''
    for a in a_elements:
        class_name = a.get('class')
        if class_name == ['right', 'file_page_2']:
            transcript1 = a.get('href')
        if class_name == ['right', 'file_page_5']:
            transcript2 = a.get('href')
    return transcript1, transcript2


def get_links():
    youtube1 = ''
    vocabulary = ''
    youtube2 = ''

    for iframe in iframe_elements:
            id = iframe.get('id')
            if id == 'popup-youtube-player-page-2':
                youtube1 = iframe.get('src')
            if id == 'popup-youtube-player-page-7':
                youtube2 = iframe.get('src')
            if id == 'player':
                vocabulary = iframe.get('src')

for i in range(1, 200):
    try:
        driver.get('http://homework.topicanative.edu.vn/local/lemanager/detail.php?id={0}'.format(i))
        driver.find_element_by_xpath('/html/body/section/div/main/button').click()

        time.sleep(2)
        iframe = driver.find_element_by_xpath('/html/body/div[1]/div/div/iframe')
        driver.switch_to.frame(iframe)

        source=driver.page_source
        soup=BeautifulSoup(source,"html.parser")

        a_elements = soup.select('a')



        iframe_elements = soup.select('iframe')



driver.close()
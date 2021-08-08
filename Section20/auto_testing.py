from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
button = chrome_browser.find_element_by_class_name('btn-default')

input = chrome_browser.find_element_by_id('user-message')
input.send_keys('I AM SO COOOOL')
button.click()

message = chrome_browser.find_element_by_id('display')
assert 'I AM SO COOOOL' in message.text

chrome_browser.quit()
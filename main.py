from selenium import webdriver
import os

EMAIL = os.environ['email']
PASSWORD = os.environ['password']
POGO_KEY = os.environ['pogo']


def send_text(element, text: str) -> None:
    element.clear()
    element.click()
    element.send_keys(text)


profile = webdriver.FirefoxProfile()
options = webdriver.FirefoxOptions()


profile.set_preference('geo.prompt.testing', True)
profile.set_preference('geo.prompt.testing.allow', True)
profile.set_preference('geo.wifi.uri',
                       'data:application/json,{"location": {"lat": 40.7590, "lng": -73.9845}, "accuracy": 100.0}')

driver = webdriver.Firefox(firefox_profile=profile)
driver.get('https://pogotrainer.club/')

elem = driver.find_element_by_id('loginDropDown')
elem.click()

elem = driver.find_element_by_class_name('form-control')
send_text(elem, EMAIL)

elem = driver.find_element_by_name('loginPassword')
send_text(elem, PASSWORD)

elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary pull-left")]')
elem.click()


driver.get('https://pogotrainer.club/account/')

elem = driver.find_element_by_xpath('//a[contains(@class, "btn btn-sm btn-primary")]')
elem.click()

elem = driver.find_element_by_id('updateFriendCodeBtn')
elem.click()

elem = driver.find_element_by_name('PDPID')
elem.click()

elem.send_keys(POGO_KEY)

elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary")]')
elem.click()

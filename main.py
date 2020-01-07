from selenium import webdriver
import os

EMAIL = os.environ['email']
PASSWORD = os.environ['password']
POGO_KEY = os.environ['pogo']
WEB = 'https://pogotrainer.club/'
ACCOUNT = 'https://pogotrainer.club/account/'
HEADLESS = True


def log(msg):
    print(msg)


def send_text(element, text: str) -> None:
    element.clear()
    element.click()
    element.send_keys(text)


profile = webdriver.FirefoxProfile()
options = webdriver.FirefoxOptions()
options.headless = HEADLESS

profile.set_preference('geo.prompt.testing', True)
profile.set_preference('geo.prompt.testing.allow', True)
profile.set_preference('geo.wifi.uri',
                       'data:application/json,{"location": {"lat": 40.7590, "lng": -73.9845}, "accuracy": 100.0}')

log(f'Joining {WEB}')
driver = webdriver.Firefox(firefox_profile=profile, options=options)
driver.get(WEB)

elem = driver.find_element_by_id('loginDropDown')
elem.click()

log('Inputing email')
elem = driver.find_element_by_class_name('form-control')
send_text(elem, EMAIL)

log('Inputing password')
elem = driver.find_element_by_name('loginPassword')
send_text(elem, PASSWORD)

elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary pull-left")]')
elem.click()

log('Sucess')
log('Going to account settings')
driver.get(ACCOUNT)

log(f'Updating code {POGO_KEY}')
elem = driver.find_element_by_xpath('//a[contains(@class, "btn btn-sm btn-primary")]')
elem.click()

elem = driver.find_element_by_id('updateFriendCodeBtn')
elem.click()

elem = driver.find_element_by_name('PDPID')
elem.click()

elem.send_keys(POGO_KEY)

elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary")]')
elem.click()
log('Success, closing now')

driver.close()

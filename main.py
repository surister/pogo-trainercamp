import os
from json import load
from selenium import webdriver
import time

with open('./setup.json', 'r') as f:
    env_variables = load(f)

WEB = 'https://pogotrainer.club/'
ACCOUNT = 'https://pogotrainer.club/account/'

if env_variables['email'] == 'fakemail@gmail.com':
    raise ValueError('Environment variables are not set, check setup.json file')


"""
{
  "email": "fakeemail@gmail.com",
  "password": "fakepassword",
  "pogo_key": "0000 0000 0000",
  "headless": false,
  "cooldown": 300,
  "total_time": 0,
  "_comment": "'headless' can either be true or false (default), ",
  "_comment2": "Respect the spaces between numbers in 'pogo_key'   2334 9834 3723 is valid, 233498343723 IS NOT ",
  "_comment3": "Cooldown is the time between execution, I recommend 300 seconds (default, 5 minutes) not less than 1 minute",
  "_comment4": "Total time is for how long the script will run, 0 is forever or until you close the script, time is in secconds.",
  "_comment5": "Only 'email', 'password', 'pogo_key', 'headless', 'cooldown', 'total_time' should be modified by user"
}
"""


def log(msg):
    print(f'Logging -> {msg}')


def main():

    def send_text(element, text: str) -> None:
        element.clear()
        element.click()
        element.send_keys(text)

    profile = webdriver.FirefoxProfile()
    options = webdriver.FirefoxOptions()
    options.headless = env_variables['headless']

    profile.set_preference('geo.prompt.testing', True)
    profile.set_preference('geo.prompt.testing.allow', True)
    profile.set_preference('geo.wifi.uri',
                           'data:application/json,{"location": {"lat": 40.7590, "lng": -73.9845}, "accuracy": 100.0}')

    log(f'Joining {WEB}')
    driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path='./geckodriver.exe')
    driver.get(WEB)

    elem = driver.find_element_by_id('loginDropDown')
    elem.click()

    log('Inputing email')
    elem = driver.find_element_by_class_name('form-control')
    send_text(elem, env_variables['email'])

    log('Inputing password')
    elem = driver.find_element_by_name('loginPassword')
    send_text(elem, env_variables['password'])

    elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary pull-left")]')
    elem.click()

    log('Success')
    log('Going to account settings')
    driver.get(ACCOUNT)

    log(f'Updating code {env_variables["pogo_key"]}')
    elem = driver.find_element_by_xpath('//a[contains(@class, "btn btn-sm btn-primary")]')
    elem.click()

    elem = driver.find_element_by_id('updateFriendCodeBtn')
    elem.click()

    elem = driver.find_element_by_name('PDPID')
    elem.click()

    elem.send_keys(env_variables["pogo_key"])

    elem = driver.find_element_by_xpath('//input[contains(@class, "btn btn-primary")]')
    elem.click()
    log('Success, closing now')
    time.sleep(1)

    driver.close()
    log(f'Will wait {env_variables["cooldown"]}')

    time.sleep(env_variables['cooldown'])


if __name__ == '__main__':
    before = time.time()

    while True:

        main()
        now = time.time() - before

        print(now)
        if now <= env_variables['total_time']:
            log(f'The script has been running for {now} seconds')

        if env_variables['total_time'] == 0:
            pass

        else:
            if now >= env_variables['total_time'] - env_variables['cooldown']:  # Fix me, time always gonna be less that given
                print(f'Reached maximum time, closing')
                exit(0)

from selenium import webdriver

profile = webdriver.FirefoxProfile()

profile.set_preference("geo.prompt.testing", True)
profile.set_preference("geo.prompt.testing.allow", True)
profile.set_preference('geo.wifi.uri',
                       'data:application/json,{"location": {"lat": 40.7590, "lng": -73.9845}, "accuracy": 27000.0}')


driver = webdriver.Firefox(firefox_profile=profile)

driver.get('https://www.where-am-i.net/')

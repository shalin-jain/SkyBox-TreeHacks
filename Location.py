from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time


def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)
    driver.get("https://www.gps-coordinates.net/my-location")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="lng"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    longitude = longitude.split(' ')
    longitude = longitude[0]
    latitude = driver.find_elements_by_xpath('//*[@id="lat"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    latitude = latitude.split(' ')
    latitude = latitude[0]
    driver.quit()
    return (latitude, longitude)


print(getLocation())
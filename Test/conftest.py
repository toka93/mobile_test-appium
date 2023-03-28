import pytest
from appium import webdriver
import json
import os.path as path
from ReusableScreens.HomePage import HomePage
import platform


@pytest.fixture
def driver():
    print(platform.system())
    if (platform.system() == 'Windows'):
        f = open('Data'+path.sep + 'androidCap.json')
        data = json.load(f)
        desired_caps = {
            "platformName": data['platformName'],
            "appium:platformVersion": data['platformVersion'],
            "appium:deviceName": data['deviceName'],
            "appium:app":  data['app'],
            "appium:appActivity":  data['appActivity'],
            "appium:appPackage":  data['appPackage']}
    
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(600)
    yield driver





@pytest.fixture()
def homePage(driver):

    return HomePage(driver)




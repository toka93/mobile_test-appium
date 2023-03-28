from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)



    def split_locator(self,locator):
        result = ()
        "Split the locator type and locator"
        result = tuple(locator.split(',',1))
        return result
        
    def createElement(self,value):
        el=self.split_locator(value)
        locatorType=el[0]
        match locatorType :
            case "ID" :
              element = self.driver.find_element(AppiumBy.ID,el[1]) 
            case "ACCESSIBILITY_ID" :
              element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID,el[1]) 
            case "CLASS_NAME" :
              element = self.driver.find_element(AppiumBy.CLASS_NAME,el[1]) 
            case "XPATH" :
              element = self.driver.find_element(AppiumBy.XPATH,el[1])
            

        return element
    
    def clickButton(self,element):
        try:
          element.click()
        except Exception as e:
            print("click exception :"+ e)   

    def getText(self,element):
        try:
          txt= element.text
        except Exception as e:
            print("Get text exception :"+ e) 
        return  txt
    
   

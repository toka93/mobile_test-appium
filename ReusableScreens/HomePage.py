from ReusableScreens.BasePage import BasePage 
import ReusableScreens.Locators_conf as Locator
from selenium.webdriver.support.expected_conditions import staleness_of


class HomePage(BasePage):

   def __init__(self, driver):
        self.driver = driver
        
  
   def ClickOnThree(self):
       three=self.createElement(getattr(Locator, "numThree"))
       self.clickButton(three)

   def ClickOnTwo(self) :  
       two=self.createElement(getattr(Locator, "numTwo"))
       self.clickButton(two)

   def ClickOnAdd(self):    
       add_El=self.createElement(getattr(Locator, "add"))
       self.clickButton(add_El)
    
   def ClickOnSubtract(self):    
       sub_El=self.createElement(getattr(Locator, "sub"))
       self.clickButton(sub_El)

   def getResult(self):  
       equal=self.createElement(getattr(Locator,"equal"))
       self.clickButton(equal)
       res=self.createElement(getattr(Locator,"result"))
       print(self.getText(res))
       return self.getText(res)







   

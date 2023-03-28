import pytest
import pytest_html
import json
import os.path as path
from appium import webdriver








def test_Summation(homePage):

   
    homePage.ClickOnThree()
    homePage.ClickOnAdd()
    homePage.ClickOnTwo()
    value=homePage.getResult()
  
    assert value=='5'

   
    



def test_resetapp(homePage):
    
    homePage.ClickOnThree()
    homePage.ClickOnSubtract()
    homePage.ClickOnTwo()
    value=homePage.getResult()
  
    assert value=='1'
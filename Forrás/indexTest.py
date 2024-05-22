# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# set driver
browser = webdriver.Edge()
browser.get('http://127.0.0.1:5500/Forr%C3%A1s/index.html')
# functions

# test1: dupla kattintás után szerepel-e az "animation" class
def elementOne():
    time.sleep(1)
    elementOne=browser.find_element(By.ID, value="element-one")
    assert 
# ha rámegy az egér, utána létezik-e box-shadow
def elementTwo():
       time.sleep(1)
       elementTwo=browser.find_element(By.ID, value="element-two")
       assert 
# kattintás után eltűnik-e
def elementThree():
     time.sleep(1)
     elementThree=browser.find_element(By.ID, value="element-three")
     assert
# kattintás után a háttere zöld lesz-e
def elementFour(color):
    time.sleep(1)
    elementFour=browser.find_element(By.ID, value="element-four")
    assert f"background-color: {color}" in elementFour.get_attribute("style")


# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
elementFour()
browser.save_screenshot("negyesteszt.png")

import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./chromedriver.exe')


driver.get('http://127.0.0.1:8777')


score = driver.find_element(By.ID,"score").text
def scoreinrange():
    if 1<int(score)<1000:
        inrange=True
    else:
        inrange=Flase
    return inrange
test=scoreinrange()
if test==True:
    sys.exit(0)
else:
    sys.exit(1)

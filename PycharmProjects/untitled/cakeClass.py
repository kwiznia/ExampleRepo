__author__ = 'kwiznia'
from selenium import webdriver

class url():
    driver = webdriver.Firefox()
    driver.get("http://www.cheesecake.com/Cakes-9-Inch.asp")
    driver.implicitly_wait(10)
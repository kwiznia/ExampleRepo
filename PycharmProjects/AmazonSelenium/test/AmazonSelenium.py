__author__ = 'kwiznia'
from lettuce import *
from selenium import webdriver
from selenium.webdriver import ActionChains

@step('I go to URL')
def go_to_URL(step):
    driver = webdriver.Firefox()
    driver.get("http://www.amazon.co.uk/")
    element = driver.find_element_by_xpath("/html/body/div[3]/div/div[4]/div[2]/table/tbody/tr/td/map/area")
    target = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[2]/div[3]/form/div[2]/div/input")
    ActionChains(driver).drag_and_drop(element, target).perform()
    button = driver.find_element_by_xpath("/html/body/header/div/div[2]/div[2]/div[3]/form/div/input").click()
    assert "No results found." not in driver.page_source


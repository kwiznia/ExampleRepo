__author__ = 'kwiznia'
from lettuce import *
from selenium import webdriver
from selenium.common.exceptions import ElementNotSelectableException

driver = webdriver.Firefox()
driver.get("http://www.cheesecake.com/Cakes-9-Inch.asp")
driver.implicitly_wait(10)

@step('I click somewhere')
def click_somewhere(step):
    element = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[3]/div[3]/div/div[2]/div/table/tbody/tr/td/div/div/a/img").click()
    #assert "No results found." not in driver.page_source

@step('I fill the text field')
def fill_the_text_field(step):
    quantityText = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div/div[2]/table/tbody/tr/td[2]/input")
    quantityText.clear()
    quantityText.send_keys(3)
    zipCodeText = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div/div[2]/table/tbody/tr[3]/td[2]/div/div/input")
    zipCodeText.clear()
    zipCodeText.send_keys(10023)

@step('I select element from the box')
def select_element_from_the_box(step):
    select = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div/div[2]/table/tbody/tr[5]/td/select/option[4]").click()
    ElementNotSelectableException(msg=None, screen=None, stacktrace=None)

@step('I press the bottom')
def press_the_bottom(step):
    addToCartButton = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[4]/div/div[2]/table[2]/tbody/tr/td/a/span").click()
    #driver.back()
    driver.close()
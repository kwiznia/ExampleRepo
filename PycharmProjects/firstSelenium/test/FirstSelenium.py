__author__ = 'kwiznia'
from lettuce import *
from selenium import webdriver

@step('I go to URL')
def go_to_URL(step):
    driver = webdriver.Firefox() #create the instance
    driver.get("http://www.google.com") #this method will navigate to the page
    #I take the xpath of the box and save it on element
    element = driver.find_element_by_xpath("/html/body/div/div[2]/div/div/div[3]/div/div/div/form/fieldset[2]/div/div/div/div/div[3]/div/input")
    element.send_keys("some text")
    assert "No results found." not in driver.page_source #if the page doesnt exist, then send a message
    #driver.close()
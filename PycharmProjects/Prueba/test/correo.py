__author__ = 'kwiznia'
from lettuce import *
from selenium import webdriver

class correo():

    driver = webdriver.Firefox()
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1")

    # Escribimos nuestro usuario
    user = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/form/input[14]")
    user.send_keys("alvarorm89@gmail.com")

    #Escribimos nuestro contrasena
    pswd = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/form/input[15]")
    pswd.send_keys("widowmaker")


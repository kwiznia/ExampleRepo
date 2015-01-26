from lettuce import *
from selenium import webdriver

class correo():

    driver = webdriver.Firefox()
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1")

    # Escribimos nuestro usuario
    usuario = driver.find_element_by_xpath("//*[@id='Email']")
    usuario.sendKeys("alvarorm89@gmail.com")

    #Escribimos nuestro contrasena
    driver.find_element_by_xpath("//*[@id='Passwd']").sendKeys("widowmaker")

    #Desactivamos No cerrar sesion
    driver.find_element_by_xpath("//*[@id='PersistentCookie']").click()

    #Pulsamos iniciar sesion
    driver.find_element_by_xpath(".//*[@id='signIn']").click()

    #Esperamos
    driver.implicitly_wait(5)

    elemento = driver.find_element_by_xpath("html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div")

    def __getboton__(self):
        return self.elemento.text
__author__ = 'kwiznia'
from selenium import webdriver


class correo():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def openpage(self):
        self.driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive"
                        "=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1"
                        "&ltmpl=default&ltmplcache=2&emr=1")

    def writeusername(self):
        user = self.driver.find_element_by_xpath("//*[@id='Email']")
        user.send_keys("alvarorm89@gmail.com")

    def writepswd(self):
        self.driver.find_element_by_xpath("//*[@id='Passwd']").send_keys("********")

    def pressbutton(self):
        self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/form/input[16]").click()

    def checkbutton(self):
        button = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div/div").text
        return button

    def closepage(self):
        self.driver.close()

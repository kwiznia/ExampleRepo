__author__ = 'kwiznia'
import requests

class weather():

    def openpage(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk')
        return r

    def gettemperature(self):
        print(self.openpage().text)

		
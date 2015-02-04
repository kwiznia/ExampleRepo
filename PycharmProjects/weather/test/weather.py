__author__ = 'kwiznia'
import requests
from lettuce import world

class weather():

    def getWeather(self, url):
        world.url = url
        world.url = requests.get(url)
        return world.url

    def getCity(self, city):
        c = city
        return c

    def openpage(self, url):
        return world.url.status_code

    def gettemperature(self, url):
        print(world.url.text)

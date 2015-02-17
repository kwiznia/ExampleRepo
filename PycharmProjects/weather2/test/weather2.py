__author__ = 'kwiznia'
import requests
from lettuce import world
import json

class weather2():

    def getStatus_code(self, url):
        world.url = url
        world.url = requests.get(url)
        return world.url.status_code

    def getInformation(self, url):
        world.url = url
        world.url = requests.get(url)
        return world.url.text
		
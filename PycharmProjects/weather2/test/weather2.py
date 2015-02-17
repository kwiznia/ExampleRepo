__author__ = 'kwiznia'
import requests
from lettuce import world
import json

class weather2():

    """
   def getStatus_code(self, url):
        world.url = url
        result = requests.get(url)
        return result.status_code
    """

    def getInformation(self, url):
        world.url = url
        result = requests.get(url)
        return result.json()

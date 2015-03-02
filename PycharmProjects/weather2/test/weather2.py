__author__ = 'kwiznia'
import requests
from lettuce import world
import json

class weather2():
    """
    def getStatus_code(self, response):
        world.response = response
        world.response = requests.get(response)
        return world.response.status_code
    """

    def getInformation(self, url, format):
        world.response = requests.get(url, headers={'Accept': format})
        return world.response.json()

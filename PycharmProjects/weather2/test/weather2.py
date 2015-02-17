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

    def getInformation(self, response):
        world.response = response
        world.response = requests.get(response)
        world.status_code = world.response.status_code
        return world.response.json()
		
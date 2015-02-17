__author__ = 'kwiznia'
import requests
from lettuce import world

class weather():

    def getStatus_code(self, url):
        world.url = url
        world.url = requests.get(url)
        return world.url.status_code

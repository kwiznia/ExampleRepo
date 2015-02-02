__author__ = 'kwiznia'

from lettuce import *
from weather import *
from nose.tools import *

weather = weather()

@step("I access the url")
def accessUrl(self):
    assert_equals(weather.openpage().status_code, 200), "Error, page not found"

@step(" I get the temperature in centigrade")
def getTemperature(self):
   assert_is_none(weather.gettemperature(), "The weather information is empty")
   
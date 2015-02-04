__author__ = 'kwiznia'

from lettuce import *
from weather import *
from nose.tools import *

weather = weather()

@step("I access the url with (.*)")
def accessUrl(self, expectedUrl):
    world.expectedUrl = expectedUrl
    assert_not_equals(weather.getWeather(world.expectedUrl), None), "The page is empty"

@step("And the city with (.*)")
def cityname(self, expectedCity):
    world.expectedCity = expectedCity
    assert_not_equals(weather.getCity(expectedCity), None), "Empty city name"

@step("I ask for weather information")
def getweatherinformation(self):
    assert_equals(weather.openpage(world.expectedUrl), 200), "page not found"
    #print(weather.openpage(world.expectedUrl))

@step("I get the temperature in centigrade")
def getweathertemperature(self):
    assert_is_none(weather.gettemperature(world.expectedUrl), "The weather information is empty")

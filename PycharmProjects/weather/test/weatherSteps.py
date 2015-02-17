__author__ = 'kwiznia'

from lettuce import *
from weather import *
from nose.tools import *

weather = weather()

@step("I access the url with (.*)")
def accessUrl(self, expectedUrl):
    world.expectedUrl = expectedUrl
    assert_regexp_matches(world.expectedUrl, '^http'), "The URL is empty"

@step("And the city is (.*) and the country (.*)")
def cityname(self, expectedCity, expectedCountry):
    world.expectedCity = expectedCity
    world.expectedCountry = expectedCountry
    assert_in(expectedCity, ["Madrid", "London", "Barcelona", "Berlin"]), "Empty or wrong city name"
    assert_in(expectedCountry, ["UK", "Spain", "Germany"]), "Empty or wrong country name"

@step("And the latitude is (.*) and the longitude (.*)")
def cityname(self, expectedLatitude, expectedLongitude):
    world.expectedLatitude = expectedLatitude
    world.expectedLongitude = expectedLongitude
    assert_in(expectedLatitude, ["40", "35", "41.3", "52.5"]), "Empty or wrong latitude"
    assert_in(expectedLongitude, ["-3.7", "139", "2.1", "13.3"]), "Empty or wrong longitude"

@step("I ask for page information")
def getweatherinformation(self):
    world.url = world.expectedUrl + "?" + world.expectedCity + "," + world.expectedCountry
    world.status_code = weather.getStatus_code(world.url)

@step("I check if the page is ok")
def getweathertemperature(self):
    assert_equals(world.status_code, 200), "page not found"
    #compruebo que lo que me devolvio el step anterior esta bien

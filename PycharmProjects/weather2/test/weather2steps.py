__author__ = 'kwiznia'

from lettuce import *
from weather2 import *
from nose.tools import *

weather2 = weather2()

@step("I access the url with (.*)")
def access_url(self, expectedUrl):
    world.expectedUrl = expectedUrl
    assert_regexp_matches(world.expectedUrl, '^http'), "The URL is empty"

@step("the city is (.*) and the country (.*)")
def check_city_and_country(self, expectedCity, expectedCountry):
    world.expectedCity = expectedCity
    world.expectedCountry = expectedCountry

@step("I ask for the city and country name")
def page_information_by_city(self):
    world.url = world.expectedUrl + "?q=" + world.expectedCity + "," + world.expectedCountry
    world.page_code_city = weather2.getStatus_code(world.url)

@step("I check if the city and country are correct")
def check_city_and_country_values(self):
    assert_in(world.expectedCity, ["Madrid", "London", "Barcelona", "Berlin"]), "Empty or wrong city name"
    assert_in(world.expectedCountry, ["UK", "ES", "Germany"]), "Empty or wrong country name"

@step("I check if the status code of the page look by city and country is 200")
def get_page_code(self):
    assert_equals(world.page_code_city, 200), "page not found"

@step("the latitude is (.*) and the longitude (.*)")
def check_lat_and_long(self, expectedLatitude, expectedLongitude):
    world.expectedLatitude = expectedLatitude
    world.expectedLongitude = expectedLongitude

@step("I ask for the latitude and longitude")
def page_information_latlong(self):
    world.url = world.expectedUrl + "?lat=" + world.expectedLatitude + "&lon=" + world.expectedLongitude
    world.page_code_city = weather2.getStatus_code(world.url)

@step("I check if the latitude and longitude are correct")
def check_lat_and_long_values(self):
    assert_in(world.expectedLatitude, ["40", "35", "41.3", "52.5"]), "Empty or wrong latitude"
    assert_in(world.expectedLongitude, ["-3.7", "139", "2.1", "13.3"]), "Empty or wrong longitude"

@step("I check if the status code of the page look by latitude and longitude is 200")
def get_page_code(self):
    assert_equals(world.page_code_city, 200), "page not found"

@step("I ask for weather information by city and country")
def page_information_by_city(self):
    world.url = world.expectedUrl + "?q=" + world.expectedCity + "," + world.expectedCountry
    world.page_info_by_country = weather2.getInformation(world.url)

@step("I get the temperature in centigrade look by city and country")
def get_temperature_by_city(self):
    value = world.page_info_by_country.find('"temp":')
    temperature = world.page_info_by_country[value+7:value+13]
    temperatuce_centigrades = (float(temperature) - 32) * 5/9
    assert_equals(format(temperatuce_centigrades, '.2f'), "138.46"), "that's not the right temperature"

@step("I ask for weather information by latitude and longitude")
def page_information_by_latlong(self):
    world.url = world.expectedUrl + "?lat=" + world.expectedLatitude + "&lon=" + world.expectedLongitude
    world.page_info_by_latlon = weather2.getInformation(world.url)

@step("I get the temperature in centigrade look by latitude and longitude")
def get_temperature_by_latlong(self):
    value = world.page_info_by_latlon.find('"temp":')
    temperature = world.page_info_by_latlon[value+7:value+13]
    temperature_centigrade = (float(temperature) - 32) * 5/9
    assert_equals(format(temperature_centigrade, '.2f'), "131.63"), "that's not the right temperature"

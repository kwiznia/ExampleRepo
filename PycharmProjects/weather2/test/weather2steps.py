__author__ = 'kwiznia'

from lettuce import *
from weather2 import *
from nose.tools import *

weather2 = weather2()

@step("I access the url with (.*)")
def access_url(self, expectedUrl):
    world.expectedUrl = expectedUrl
    assert_regexp_matches(world.expectedUrl, '^http'), "The URL is empty"


@step("the city is (Madrid|London|Barcelona|Berlin) and the country (UK|ES|Germany)")
def city_and_country(self, expectedCity, expectedCountry):
    world.expectedCity = expectedCity
    world.expectedCountry = expectedCountry


@step("I ask for the city and country name")
def ask_for_city_and_country(self):
    world.url = world.expectedUrl + "?q=" + world.expectedCity + "," + world.expectedCountry
    world.page_info = weather2.getInformation(world.url)


@step("I check if the city and country are correct")
def check_city_and_country_are_correct(self):
    sys = world.page_info['sys']
    assert sys != ""
    assert_in(world.page_info['name'], ["Madrid", "London", "Barcelona", "Berlin"]), "Empty or wrong city name"
    assert_in(sys['country'], ["GB", "ES", "Germany"]), "Empty or wrong country name"


@step("I check if the status code of the page look by city and country is 200")
def check_status_code(self):
    assert_equals(world.page_info['cod'], 200), "page not found"


@step("the latitude is (40|35|41.3|53.2) and the longitude (-3.7|139|2.1|13.3)")
def check_lat_and_long(self, expectedLatitude, expectedLongitude):
    world.expectedLatitude = expectedLatitude
    world.expectedLongitude = expectedLongitude


@step("I ask for the latitude and longitude")
def ask_for_lat_and_long(self):
    world.url = world.expectedUrl + "?lat=" + world.expectedLatitude + "&lon=" + world.expectedLongitude
    world.page_info = weather2.getInformation(world.url)


@step("I check if the latitude and longitude are correct")
def check_lat_and_long_are_correct(self):
    latlon = world.page_info['coord']
    assert latlon['lon'] != ""
    assert latlon['lat'] != ""
    assert_in(latlon['lon'], [-3.7, 139, 2.1, 13.3]), "Empty or wrong longitude"
    assert_in(latlon['lat'], [40, 35, 41.3, 52.5]), "Empty or wrong latitude"

@step("I check if the status code of the page look by latitude and longitude is 200")
def check_status_code(self):
    assert_equals(world.page_info['cod'], 200), "page not found"


@step("I ask for weather information by city and country")
def ask_for_weather_information_by_city(self):
    world.url = world.expectedUrl + "?q=" + world.expectedCity + "," + world.expectedCountry
    world.page_info_by_country = weather2.getInformation(world.url)


@step("I get the temperature look by city and country")
def get_temperature_by_city(self):
    temperature = world.page_info_by_country['main']
    temperatuce_farenhait = temperature['temp']
    assert temperatuce_farenhait != ""


@step("I ask for weather information by latitude and longitude")
def page_information_by_latlong(self):
    world.url = world.expectedUrl + "?lat=" + world.expectedLatitude + "&lon=" + world.expectedLongitude
    world.page_info_by_latlon = weather2.getInformation(world.url)


@step("I get the temperature look by latitude and longitude")
def get_temperature_by_latlong(self):
    temperature = world.page_info_by_latlon['main']
    temperatuce_farenhait = temperature['temp']
    assert temperatuce_farenhait != ""
	
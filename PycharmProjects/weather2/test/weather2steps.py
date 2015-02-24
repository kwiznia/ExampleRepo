__author__ = 'kwiznia'

from lettuce import *
from weather2 import *
from nose.tools import *

weather2 = weather2()

@step("I access the url with (.*)")
def access_url(self, expectedUrl):
    world.expectedUrl = expectedUrl
    assert_regexp_matches(world.expectedUrl, '^http'), "The URL is empty"


@step('the city is (Madrid|London|Barcelona|Berlin) and the country (GB|ES|Germany)')
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
    assert world.expectedCity in world.page_info['name']
    assert world.expectedCountry in sys['country']


@step("I check if the status code is 200")
def check_status_code(self):
    assert_equals(world.response.status_code, 200), "page not found"


@step("the latitude is (51.51|40.42|10.13) and the longitude (-0.13|3.7|-64.7)")
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
    assert_equals(float(world.expectedLatitude), latlon['lat'])
    assert_equals(float(world.expectedLongitude), latlon['lon'])


@step("I get the temperature look by city and country")
def get_temperature_look_by_city(self):
    temperature = world.page_info['main']
    temperatuce_farenhait = temperature['temp']
    assert temperatuce_farenhait != ""


@step("I ask for weather information by latitude and longitude")
def ask_for_weather_information_by_latlong(self):
    world.url = world.expectedUrl + "?lat=" + world.expectedLatitude + "&lon=" + world.expectedLongitude
    world.page_info_by_latlon = weather2.getInformation(world.url)


@step("I get the temperature look by latitude and longitude")
def get_temperature_by_latlong(self):
    temperature = world.page_info_by_latlon['main']
    temperatuce_farenhait = temperature['temp']
    assert temperatuce_farenhait != ""
	
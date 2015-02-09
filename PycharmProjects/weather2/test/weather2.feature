Feature: Check if the weather service works properly
    In order to check the weather service
    As beginner
    I'll get some values and check if they are ok and if the temperature given is correct

Scenario: Check if a city and a country given are correct
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the city is London and the country UK
    When I ask for the city and country name
    Then I check if the city and country are correct
    And I check if the status code of the page look by city and country is 200

Scenario: Check if a latitude and longitude given are correct
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the latitude is 35 and the longitude 139
    When I ask for the latitude and longitude
    Then I check if the latitude and longitude are correct
    And I check if the status code of the page look by latitude and longitude is 200

Scenario: Check if the temperature is correct given a city and a country
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the city is Madrid and the country ES
    When I ask for weather information by city and country
    Then I get the temperature in centigrade look by city and country

Scenario: Check if the temperature is correct given the latitude and longitude
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the latitude is 35 and the longitude 139
    When I ask for weather information by latitude and longitude
    Then I get the temperature in centigrade look by latitude and longitude

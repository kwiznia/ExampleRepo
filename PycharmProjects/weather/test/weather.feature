Feature: Check if the weather service works properly
    In order to check the weather service
    As beginner
    I'll get the the status code of a web page

Scenario: Check if the url of the weather service works properly given a city and a country
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the city is London and the country UK
    When I ask for page information
    Then I check if the page is ok

Scenario: Check if the url of the weather service works properly given the latitude and longitude
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the latitude is 35 and the longitude 139
    When I ask for page information
    Then I check if the page is ok


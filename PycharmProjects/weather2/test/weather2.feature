Feature: Check if the weather service works properly
    In order to check the weather service
    As beginner
    I'll get some values and check if they are ok and if the temperature given is correct

Scenario Outline: Check if a city and and country given are correct
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the city is <city> and the country <country>
    When I ask for the city and country name
    Then I check if the city and country are correct
    And I check if the status code is 200

  Examples:
    | city      | country |
    | London    | GB      |
    | Madrid    | ES      |
    | Barcelona | ES      |

Scenario Outline: Check if a latitude and longitude given are correct
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the latitude is <latitude> and the longitude <longitude>
    When I ask for the latitude and longitude
    Then I check if the latitude and longitude are correct
    And I check if the status code is 200

  Examples:
    | latitude | longitude |
    | 51.51    | -0.13     |
    | 40.42    | 3.7       |
    | 10.13    | -64.7     |

Scenario Outline: Check if the temperature is correct given a city and a country
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the city is <city> and the country <country>
    When I ask for the city and country name
    Then I get the temperature look by city and country

  Examples:
    | city      | country |
    | London    | GB      |
    | Madrid    | ES      |
    | Barcelona | ES      |

Scenario Outline: Check if the temperature is correct given the latitude and longitude
    Given I access the url with http://api.openweathermap.org/data/2.5/weather
    And the latitude is <latitude> and the longitude <longitude>
    When I ask for weather information by latitude and longitude
    Then I get the temperature look by latitude and longitude

  Examples:
    | latitude | longitude |
    | 51.51    | -0.13     |
    | 40.42    | 3.7       |
    | 10.13    | -64.7     |


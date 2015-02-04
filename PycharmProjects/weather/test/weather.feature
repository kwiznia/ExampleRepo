Feature: Check if the weather service works properly
    In order to check the weather service
    As beginner
    I'll get the temperature of a city

Scenario: Check if the url of the weather service works properly
    Given I access the url with http://api.openweathermap.org/data/2.5/weather?q=London,uk
    And the city with "London"
    When I ask for weather information
    Then I get the temperature in centigrade
        | url | city |
        | http://api.openweathermap.org/data/2.5/weather?q=London,uk | London |

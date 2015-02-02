Feature: Weather temperature
    In order to play with Lettuce
    As beginners
    We'll get the temperature of a city

Scenario: Main Page works
    Given I access the url
    When I write the name of the city <city>
    Then I get the temperature in centigrade

Examples:
| 'London' |

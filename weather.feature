Feature: Access to an URL

Scenario: Main Page works
    Given I access the url
    When I write the name of the city <city>
    Then I get the temperature in centigrade

Examples:
| 'London' |
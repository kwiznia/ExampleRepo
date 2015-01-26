Feature: Access to an URL

Scenario: Main Page works
    Given I access url "/" to get some content
    Then I use the post method

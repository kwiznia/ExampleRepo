Feature: Split a string into multiple lines on spaces
    In order to make strings more readable
    As a user
    I want to have words split into their own lines

Scenario: Split small-ish string
    Given I have the string "one two three four five"
    When I ask to have the string split into lines
    Then I should see the following:
    """
    one
    two
    three
    four
    five
    """

Scenario: check variable
    When I exemplify "world" by seeing that some variable contains "yay!"


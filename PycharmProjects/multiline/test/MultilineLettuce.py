__author__ = 'kwiznia'
from lettuce import *

@step('I should see the following:')
def i_should_see_the_following(step):
    assert step.multiline == """one
    two
    three
    four
    five"""

@step('I have the string "one two three four five"')
def i_have_the_string_one_two_three_four_five(step):
    assert True

@step('I ask to have the string split into lines')
def i_ask_to_have_the_string_split_into_lines(step):
    assert True

@step(r'exemplify "world" by seeing that some variable contains "(.*)"')
def exemplify_world(step, value):
    world.some_variable = "yay!"
    assert world.some_variable == value


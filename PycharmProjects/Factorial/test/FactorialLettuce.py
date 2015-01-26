__author__ = 'kwiznia'
from lettuce import *

@before.all
def say_hello():
    print "hello there"

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = (number)

@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)

@step('I see the number (\d+)')
def check_number(step, expected):
    expected = (expected)
    assert world.number == expected, \
    "Got %d" % world.number

def factorial(number):
    number = (number)
    if(number == 0) or (number == 1):
        return 1
    else:
        return number*factorial(number-1)

@after.all
def say_goodbye(total):
    print " "
    print "goodbye"

@before.each_feature
def setup_some_feature(feature):
    print "the feature %r will run" % feature.name

@after.each_feature
def teardown_some_feature(feature):
    print "the feature %r just has run" % feature.name

@before.each_scenario
def setup_each_scenario(scenario):
    print "the scenario %r will run" % scenario.name

@after.each_scenario
def teardown_some_scenario(scenario):
    print "the scenario %r just has run " % scenario.name

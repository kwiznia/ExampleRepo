__author__ = 'kwiznia'
from lettuce import *

@step('we have lettuce installed')
def step_imple(context):
    pass

@step('we implement a test')
def step_impl(context):
    assert True is not False

@step('lettuce will test it automatically')
def step_impl(context):
    assert True is True
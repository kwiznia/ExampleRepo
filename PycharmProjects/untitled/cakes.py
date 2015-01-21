__author__ = 'kwiznia'
from lettuce import *
import cakeClass

operator = cakeClass()

@step('I enter into an url')
def enter_into_url(self):
    operator
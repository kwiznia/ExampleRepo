__author__ = 'kwiznia'
from lettuce import *
from correo import *
from nose.tools import assert_equals, assert_is_none

correo = correo()

@step("open the main page")
def open_main_page(self):
    assert_equals(correo.openpage(), None), "Error, page not found"

@step("write my username")
def write_username(self):
    assert_is_none(correo.writeusername(), "The username cannot be empty")

@step("write my password")
def write_password(self):
    assert_is_none(correo.writepswd(), "The password cannot be empty")

@step("press the sign in button (.*)")
def press_sign_in_button(self, expected):
    assert str(correo.pressbutton()) != expected, "Thats not the right button"

@step("check the write new message button (.*)")
def check_button(self, expected):
    assert str(correo.checkbutton()) != expected, "You didnt press the right button"
    correo.closepage()

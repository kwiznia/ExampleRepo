__author__ = 'kwiznia'
from lettuce import *
import requests

@step(r'I access url "(.*)"')
def access_url(url,step):
    url='http://api.openweathermap.org/data/2.5/weather?q=London'
    r = requests.get(url)
    print r.headers
    print r.status_code
    print r.content
    print r.json
    print url

__author__ = 'kwiznia'
from lettuce import *
import requests

@step('I access url "(.*)"')
def access_url(url,step):
    url='http://api.openweathermap.org/data/2.5/weather?q=London'
    r = requests.get(url)
    print r.headers
    print r.status_code
    print r.content
    print r.json
    print url

@step('I use the POST method')
def use_the_post_method(step):
    payload = {'temp': '1111', 'name': 'Madrid'}
    url='http://api.openweathermap.org/data/2.5/weather?q=London'
    r=requests.put(url, payload)
    print r.text
    with url.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=London') as f:
        print(f.read(10))

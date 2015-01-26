__author__ = 'kwiznia'
from lettuce import *
import requests

@step(r'I access url "(.*)"')
def access_url(url,step):
    url='https://www.google.es/maps/place/Calle+Arturo+Soria,+90,+28027+Madrid/@40.4451275,-3.6456848,17z/data=!3m1!4b1!4m2!3m1!1s0xd422f3ccb1ddc95:0x528b51cc7f1f1b7b?hl=enhttps://www.google.es/maps/place/Calle+Arturo+Soria,+90,+28027+Madrid/@40.4451275,-3.6456848,17z/data=!3m1!4b1!4m2!3m1!1s0xd422f3ccb1ddc95:0x528b51cc7f1f1b7b?hl=en'
    r = requests.get(url)
    print r.headers
    print r.status_code
    print r.content
    print r.json
    print url

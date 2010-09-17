import os
import urllib, urllib2
try:
    import json
except ImportError:
    import simplejson as json


class AlchemyError(Exception):
    "Exception for Alchemy API"


class Alchemy(object):
    
    def __init__(self, apikey):
        self.apikey = apikey or os.environ.get('ALCHEMY_API_KEY')
    
    def url_get_text(self, url, **params):
        BASE = "http://access.alchemyapi.com/calls/url/URLGetText?"
        params['url'] = url
        params['apikey'] = self.apikey
        params['outputMode'] = "json"
        response = urllib2.urlopen(BASE + urllib.urlencode(params))
        result = json.loads(response.read())
        
        if result['status'].upper() == "ERROR":
            raise AlchemyError(result['statusInfo'])
        
        return result['text']
        



import os
import unittest
import urllib2

try:
    import json
except ImportError:
    import simplejson as json

from alchemy import Alchemy

class AlchemyTest(unittest.TestCase):
    
    def test_extract_text(self):
        url = "http://access.alchemyapi.com/calls/url/URLGetText?apikey=14a23d8025d8ef0bb71b89b5c8ea3a6c23cc84b4&url=http://www.pbs.org/newshour/rundown/2010/09/x-prize-winning-automobile.html&outputMode=json"
        result = json.loads(urllib2.urlopen(url).read())
        
        alchemy = Alchemy(os.environ.get('ALCHEMY_API_KEY'))
        
        self.assertEqual(
            result['text'],
            alchemy.url_get_text('http://www.pbs.org/newshour/rundown/2010/09/x-prize-winning-automobile.html')
        )


if __name__ == "__main__":
    unittest.main()
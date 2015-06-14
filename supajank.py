from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import error as tweepyerror
from ConfigParser import SafeConfigParser
from json import loads
from HTMLParser import HTMLParser
from time import sleep
from random import randint

# import supabotfire
import jankyaf

parser = SafeConfigParser()
parser.read('jankyaf.ini')

CONSUMER_KEY = parser.get('twitter', 'consumer.key')
CONSUMER_SECRET = parser.get('twitter', 'consumer.secret')
ACCESS_KEY = parser.get('twitter', 'access.key')
ACCESS_SECRET = parser.get('twitter', 'access.secret')

class StdOutListener(StreamListener):
    def __init__(self):
        # auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        # auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        # api = API(auth)
        self.processor = jankyaf.janky_af
    def on_data(self, data):
        try:
            parsed_data = loads(data)
            text = parsed_data['text']
            h = HTMLParser()
            text = h.unescape(text)
            status_id = parsed_data['id']
            message = self.processor(text, parsed_data['user']['screen_name'])
            if message == "":
                pass
            else:
                try:
                    print message
                    api.update_status(status=message, in_reply_to_status_id=status_id)
                    return False
                except tweepyerror.TweepError:
                    pass
        except KeyError:
            pass
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = API(auth)
    l = StdOutListener()
    stream = Stream(auth, l)
    while True:
        stream.filter(track=['my'])
        sleep(randint(0, 100))

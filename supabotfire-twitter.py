from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import error as tweepyerror
from ConfigParser import SafeConfigParser
from json import loads
import HTMLParser
import time

import supabotfire

parser = SafeConfigParser()
parser.read('supabotfire.ini')

CONSUMER_KEY = parser.get('twitter', 'consumer.key')
CONSUMER_SECRET = parser.get('twitter', 'consumer.secret')
ACCESS_KEY = parser.get('twitter', 'access.key')
ACCESS_SECRET = parser.get('twitter', 'access.secret')

class StdOutListener(StreamListener):
    def __init__(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = API(auth)

    def on_data(self, data):
        try:
            parsed_data = loads(data)
            text = parsed_data['text']
            h = HTMLParser.HTMLParser()
            text = h.unescape(text)
            status_id = parsed_data['id']

            message = supabotfire.supa_bot_fire(text)
            if message == "":
                pass
            else:
                message += " @" + parsed_data['user']['screen_name']
                print text
                print message
                try:
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
        stream.filter(track=['I', "we"])
        time.sleep(30*60)

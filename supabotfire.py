#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API
from tweepy import error as tweepyerror
from ConfigParser import SafeConfigParser
from json import loads
import HTMLParser
import nltk

# Read API credentials from config file

parser = SafeConfigParser()
parser.read('supabotfire.ini')

CONSUMER_KEY = parser.get('twitter', 'consumer.key')
CONSUMER_SECRET = parser.get('twitter', 'consumer.secret')
ACCESS_KEY = parser.get('twitter', 'access.key')
ACCESS_SECRET = parser.get('twitter', 'access.secret')

disallowed_verbs = ["\'m", "am", "\'ve", "wan", "cant"]
verb_forms = ["VB", "VBD", "VBP"]
banned_strings = ["Facebook", "YouTube", "http://", "https://", "www.", ".com"]

sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

class StdOutListener(StreamListener):
    def __init__(self):
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        api = API(auth)

    def on_data(self, data):
        message = ''
        try:
            parsed_data = loads(data)
            text = parsed_data['text']
            h = HTMLParser.HTMLParser()
            text = h.unescape(text)
            status_id = parsed_data['id']
            if any(banned_string in text for banned_string in banned_strings):
                pass
            else:
                try:
                    text = sentence_detector.tokenize(text.strip())[0]
                    tag_list = nltk.pos_tag(nltk.tokenize.word_tokenize(text))
                    if tag_list[0][1] == 'PRP' \
                    and tag_list[1][1] in verb_forms \
                    and not tag_list[1][0].lower() in disallowed_verbs \
                    and not tag_list[2][0] in ["n\'t"] \
                    and not any("CC" == tag[1] for tag in tag_list):
                        for tag in tag_list[2:-1]:
                            message += tag[0] + " "
                        if tag_list[-1][0] not in [',', '.', '!', '?']:
                            message += tag_list[-1][0]
                        message += ": " + tag_list[0][0] + " " + tag_list[1][0] + " that."
                        message += " @"+parsed_data['user']['screen_name']
                        print text
                        print message
                        print tag_list
                        try:
                            api.update_status(status=message, in_reply_to_status_id=status_id)
                        except tweepyerror.TweepError:
                            pass
                except IndexError:
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
        stream.filter(track=['I'])
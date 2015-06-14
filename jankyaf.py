from random import choice
import re

punctuation = ['.', ' ', ',', '\'', '\"', '(', ')']
greetings = ['yo', 'hey', 'wassup', 'ayy', '\'sup', 'ayo', 'about it', 'a-yo', 'holla', 'how\'s it hanging', 'what\'s crack-a-lackin\'', 'Greetings and salutations']
signoffs = ['keep easy', '\'ere me now', 'ya dig', 'word up', '#truth', 'peace out', 'hang loose', 'check it', 'booyakasha', 'respect', 'can ya dig it', 'ya feel me']
banned_strings = ['fitbit', 'mom', 'dad', 'mother', 'father', 'kid', 'son', 'daughter']

def janky_af(text, screen_name):
    message = ""
    if any(string in text for string in banned_strings):
        return ""
    text = re.findall(r"\w+|[^\w\s]", text, re.UNICODE)
    message = choice(greetings) + " @" + screen_name + ", your "
    for i in range(len(text) - 1):
        if text[i].lower() == "my":
            if text[i+1] in [' ', '']:
                return ""
            message += text[i+1]
            if text[i+1].endswith('s'):
                message += " are"
            else:
                message += " is"
            break
        else:
            return ""
    message += " janky as fuck, "
    message += choice(signoffs)
    return message
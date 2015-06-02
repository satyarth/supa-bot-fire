import nltk

disallowed_verbs = ["\'m", "am", "\'ve", "wan", "cant", "@"]
verb_forms = ["VB", "VBD", "VBP"]
banned_strings = ["Facebook", "YouTube", "http://", "https://", "www.", ".com"]
no_pre_space = ["n\'t", "\'re", "\'m", "na", "\'s", "!", ".", ",", "?", "!", ")", ":", '\'']
no_post_space = ["#", "@", "(", '`']
sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def mostly_caps(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    if upper > lower:
        return True
    else:
        return False

def supa_bot_fire(text): # I parse that
    message = ""
    if any(banned_string in text for banned_string in banned_strings):
        return ""
    else:
        try:
            text = sentence_detector.tokenize(text.strip())[0]
            tag_list = nltk.pos_tag(nltk.tokenize.word_tokenize(text))
            if tag_list[0][1] == 'PRP' \
            and not tag_list[0][1].lower() == "it" \
            and tag_list[1][1] in verb_forms \
            and not tag_list[1][0].lower() in disallowed_verbs \
            and not tag_list[2][0] in ["n\'t"] \
            and not any("CC" == tag[1] for tag in tag_list):
                for tag in tag_list[2:-1]:
                    if any(string == tag[0] for string in no_pre_space):
                        message = message.strip() + tag[0] + " "
                    elif any(string == tag[0] for string in no_post_space):
                        message += tag[0]
                    else:
                        message += tag[0] + " "
                if tag_list[-1][0] not in [',', '.', '!', '?']:
                    message += tag_list[-1][0]
                message = message.strip()
                message += ": " + tag_list[0][0] + " " + tag_list[1][0]
                if mostly_caps(message):
                    message += " THAT!!!"
                else:
                    message += " that."
                return message
            else:
                return ""
        except IndexError:
            return ""
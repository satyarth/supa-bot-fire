> Supa hot :fire: fire :fire:: I spit that.

## Requirements

Requires NLTK and tweepy. To install:

```
pip2 install -r requirements.txt
```

Also requires the `maxent_treebank_pos_tagger` and `punkt` packages for NLTK. To install, run the following in the python2 interpreter:

```
import nltk
nltk.download()

```
Should be self-explanatory from here.

## Configuration

Twitter API keys are stored in a file called `supabotfire.ini` which should look something like:

```
[twitter]
consumer.key = ukey
consumer.secret = usecret
access.key = utoken
access.secret = usecret
```

Get API keys [here](https://apps.twitter.com/)
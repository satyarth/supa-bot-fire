> Sweet dolla tea from McDonald's: I drink that
>
> Supa hot :fire: fire :fire:: I spit that
>
> Two and a Half Men: I watch that

## How it works

`supajank` gets a stream of tweets containing 'I' or 'we' via Twitter's [streaming API](https://dev.twitter.com/streaming/reference/post/statuses/filter). `supabotfire` looks for tweets in the format of personal pronoun followed by a verb. When it gets a hit, it restructures the sentence and tweets it back at the tweeter. Then it chills out for up to an hour.

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

> Glasses, jacket, shirt
>
> Call me glasses jacket shirt man
>
> Or call me supa hot, boy
>
> :100: degrees, leather jacket, cuz I'm supa hot, BOIIIIIIII

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

> Boom, bam, bop
>
> Badda bop boom POW :collision:
# MarkovTweets / KJVBlockchain

This is the (extremely simple) code underlying [@KJVBlockchain](https://twitter.com/KJVBlockchain) - the "Markov chain bot trained on the King James Bible & various ICO whitepapers".

Markov chain requirements:

* Python (2 or 3)
* [markovify](https://github.com/jsvine/markovify)

Run `python3 kjvico_train.py` to train and display tweets.

The repo contains the training corpus. These texts (KJV + ICOs) were originally obtained from:

* [masonicGit's ICO whitepaper collection](https://github.com/masonicGIT/ico-whitepapers)
* [Project Gutenberg KJV plain text](https://www.gutenberg.org/ebooks/10?msg=welcome_stranger)

The ICO whitepaper collection need to be converted from PDF using a tool such as [pdftotext](https://linuxappfinder.com/package/poppler-utils). Under the Debian/Ubuntu package ecosystem, this can be done with `apt install poppler`, followed by
```bash
find . -name "*.pdf" -execdir pdftotext {} {}.txt \;
cat $(find . -name "*.txt") > icos_all.txt
```


Crontab-based tweeting requirements:

* Ruby
* [twurl](https://github.com/twitter/twurl)
* [OAuth API key for Twitter account of interest](https://apps.twitter.com/app/new)


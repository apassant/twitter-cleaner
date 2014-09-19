twitter-cleaner
===============

Remove inactive Twitter followees

* Set-up virtualenv, install dependencies with `pip install -r requirements.txt`
* Create a Twitter app on https://apps.twitter.com
* Copy config.py.dist into config.py and set-up tokens from the previous steps
* Add optional whitelist + mailto address for reporting
* Run `./clean.py` to clean inactive followees (better in a crontab)

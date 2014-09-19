#!/usr/bin/env python
from cleaner import TwitterCleaner

import config

if __name__ == '__main__':
    cleaner = TwitterCleaner(config.consumer_key, config.consumer_secret,
                        config.access_token_key, config.access_token_secret,
                        config.whitelist, config.mailto)
    cleaner.run()

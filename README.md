# vicebot
Python-based Twitter bot that generates mock Vice headlines

**LOAD OAUTH SETTINGS**  
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
    settings = {
      'consumer_key': 'xxxx',
      'consumer_secret': 'xxxx',
      'access_token_key': 'xxxx',
      'access_token_secret': 'xxxx'
    }
  
**REQUIRES**

* OAuthlib  
https://github.com/requests/requests-oauthlib
* Python Twitter  
https://github.com/bear/python-twitter

Some structuring borrowed from Jeff's <a href='https://github.com/jeffThompson/RandomArtAssignmentBot'>bot</a>

This project is released under a <a href='http://creativecommons.org/licenses/by-nc-sa/3.0/'>Creative Commons BY-NC-SA License</a> - feel free to use, but <a href='mailto:mail@jeffreythompson.org'>please let me know</a>.

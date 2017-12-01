# An extensible Slackbot for Python3

We wanted an easy to use bot for Slack that could be added to with single plugin files.


## Installation ##
```
git clone https://github.com/dogsbodytech/extensible-slackbot.git slackbot
virtualenv -p python3 slackbot/venv3
source slackbot/venv3/bin/activate
pip3 install -r requirements.txt
cp slackbot/config.txt.template slackbot/config.txt
```
Edit `slackbot/config.txt` to include your bot name and api key

## Usage ##

python3 main.py

## Extending ##
Creating a plugin


## ToDo ##
- Readme.md
-- Installation
-- Usage
-- Extending
- Make extensable (kinda the point of this)
- Demonise

## Sources ##
https://www.fullstackpython.com/blog/build-first-slack-bot-python.html



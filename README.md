# An extensible Slackbot for Python3

We wanted an easy to use bot for Slack that could be added to with single plugin files.


## Installation ##
```
git clone https://github.com/dogsbodytech/extensible-slackbot.git slackbot
virtualenv -p python3 slackbot/venv3
source slackbot/venv3/bin/activate
pip3 install -r requirements.txt
cp slackbot/config.txt.example slackbot/config.txt
```
Edit `slackbot/config.txt` to include your bot name and application

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


=======
# extensible-slackbot


# Install Guide
```
 git clone git@github.com:dogsbodytech/extensible-slackbot.git
 cp config.txt.template config.txt
 vim config.txt
  Set bot name and api key
 venv -p python3 venv3
 . venv3/bin/activate
 pip install -r requirements.txt
```

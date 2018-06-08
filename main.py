#!/usr/bin/env python3
import time
import importlib
import pprint
from libs import post_message, add_reaction, parse_slack_output, bot_id_from_name, slack_client, BOT_NAME, ENABLED_MODULES

pp = pprint.PrettyPrinter(indent=4)

# Import all enabled modules and store them in a big overly complex dict
modules = {}
for module in ENABLED_MODULES:
    modules[module] = {}
    modules[module]['module'] = importlib.import_module('plugins.{}'.format(module))
    modules[module]['functions'] = {}
    modules[module]['functions']['at_bot_reply'] = []
    modules[module]['functions']['msg_contains_reply'] = []
    modules[module]['functions']['msg_contains_react'] = []
    objects = dir(modules[module]['module'])
    for object in objects:
        for function_type in modules[module]['functions']:
            if object.startswith(function_type):
                modules[module]['functions'][function_type].append(getattr(modules[module]['module'], object))

print('Loaded the following modules:')
pp.pprint(modules)

READ_WEBSOCKET_DELAY = 2

#print(message_reply)
#print(message_react)
#print(at_me_and_message_starts_with)
def handle_message(message, channel, user, timestamp):
    # We currently pass every single message to every function
    # I intend to have specific prefixes that are checked each time
    # so that only starts with and contains are passed the message
    # if the suffix of their function name is contained in the message
    if "<@" + BOT_ID + ">" in message: # We have been @ messaged in a channel
        message = message.replace("<@" + BOT_ID + ">",'').strip().lower()
        for module in modules:
            for function in modules[module]['functions']['at_bot_reply']:
                to_post = function(message)
                if to_post:
                    post_message(channel, to_post)

    if channel.startswith("D") and user != BOT_ID: # We have been DM'd (ignooring ourself)
        post_message(channel, "I'm sorry Dave, I'm afraid I can't do that.")

    for module in modules:
        for function in modules[module]['functions']['msg_contains_reply']:
            if function.__name__.replace('msg_contains_reply', '') in message:
                to_post = function(message)
                if to_post:
                    post_message(channel, to_post)

        for function in modules[module]['functions']['msg_contains_react']:
            if function.__name__.replace('msg_contains_react', '') in message:
                to_react = function(message)
                if to_react:
                    add_reaction(channel, timestamp, to_react)

if __name__ == "__main__":
    BOT_ID = bot_id_from_name(BOT_NAME)
    if BOT_ID == '':
        print("Could not find bot user with the name " + BOT_NAME + ": Exiting")
        exit(1)
    if slack_client.rtm_connect():
        print("DogsBOT connected and running!")
        while True:
            message, channel, user, timestamp = parse_slack_output(slack_client.rtm_read())
            if message and channel and user:
                handle_message(message, channel, user, timestamp)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

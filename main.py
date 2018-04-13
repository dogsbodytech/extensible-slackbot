#!/usr/bin/env python3
import time
import sys
from libs import *
import plugins
from plugins import *

message_reply = []
message_react = []
at_me_and_message_starts_with = []
for module in sys.modules:
    if module.startswith('plugins.'):
        for function in dir(sys.modules[module]):
            if function.startswith('message_reply'):
                message_reply.append([module, function])
            elif function.startswith('message_react'):
                message_react.append([module, function])
            elif function.startswith('at_me_and_message_starts_with'):
                at_me_and_message_starts_with.append([module, function])

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
        for might_start_with in at_me_and_message_starts_with:
            for list_of_functions_and_their_modules in at_me_and_message_starts_with:
                to_post = getattr(sys.modules[list_of_functions_and_their_modules[0]], list_of_functions_and_their_modules[1])(message)
                if to_post:
                    post_message(channel, to_post)
                    
    if channel.startswith("D") and user != BOT_ID: # We have been DM'd (ignooring ourself)
        post_message(channel, "I'm sorry Dave, I'm afraid I can't do that.")

    for might_start_with in message_reply:
        for list_of_functions_and_their_modules in message_reply:
            to_post2 = getattr(sys.modules[list_of_functions_and_their_modules[0]], list_of_functions_and_their_modules[1])(message)
            if to_post2:
                print("posting")
                post_message(channel, to_post2)

    for might_start_with in message_react:
        for list_of_functions_and_their_modules in message_react:
            print(sys.modules[list_of_functions_and_their_modules[0]])
            print(list_of_functions_and_their_modules[1])
            reaction = getattr(sys.modules[list_of_functions_and_their_modules[0]], list_of_functions_and_their_modules[1])(message)
            print(message)
            if reaction:
                print("reacting")
                add_reaction(channel, timestamp, reaction)

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

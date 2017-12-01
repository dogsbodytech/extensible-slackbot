import time
from libs import *
from command_quotes import *


READ_WEBSOCKET_DELAY = 2 


def handle_message(message, channel, user, timestamp):
    if "<@" + BOT_ID + ">" in message: # We have been @ messaged in a channel
        message = message.replace("<@" + BOT_ID + ">",'').strip().lower()
        if message.startswith('quote'):
            post_message(channel,get_random_quote())
        else:
            post_message(channel, "I'm sorry Dave, I'm afraid I can't do that.")
    if channel.startswith("D") and user != BOT_ID: # We have been DM'd (ignooring ourself)
        post_message(channel, "I'm sorry Dave, I'm afraid I can't do that.")
    if message.startswith('wobble'): # respond to any keywords
        post_message(channel, "wibble")
    if 'lunch' in message:
        add_reaction(channel, timestamp, "spaghetti")


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

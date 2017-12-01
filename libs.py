from slackclient import SlackClient
import configparser

config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
BOT_NAME = config.get('Bot', 'BOT_NAME')
API_TOKEN = config.get('Bot', 'API_TOKEN')

slack_client = SlackClient(API_TOKEN)


def post_message(channel, message):
    slack_client.api_call("chat.postMessage", channel=channel, text=message, as_user=True)

def add_reaction(channel, timestamp, reaction):
    slack_client.api_call("reactions.add", channel=channel, name=reaction, timestamp=timestamp)

def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        #print(output_list)   # Uncomment if you want a raw debug output of everything this bot sees
        for output in output_list:
            if output and 'text' in output and output['type'] == 'message':
                return output['text'], output['channel'], output['user'], output['ts']
    return None, None, None, None


def bot_id_from_name(botname):
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == botname:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
                return user.get('id')
    return None


if __name__ == "__main__":
    print("Don't call this script directly, this is the be imported.")


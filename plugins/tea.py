import re
import traceback
import requests
import configparser

def at_bot_reply_tea(message):
    if 'made' not in message or 'tea' not in message:
        # If people aren't making tea we don't want to know about it
        return

    try:
        brewer, count = re.match(r'(\w*) made (\w*) tea.*', message).group(1,2)
        post_tea_data(brewer, count)
        return ':realtea:'
    except Exception as e1:
        try:
            print(traceback.format_exc(e1))
        except Exception as e2:
            # Python traceback bug, this will do
            print(e1)

        return "Sorry I didn't quite catch that, try using this format:\n"\
            "$name made $number tea(s)"

def post_tea_data(brewer, count):
    count = int(count)
    config = configparser.ConfigParser()
    with open(r'config.txt') as f:
        config.readfp(f)

    influx_tea_url = config.get('Tea', 'URL')
    influx_tea_pass = config.get('Tea', 'KEY')
    influx_tea_db = config.get('Tea', 'DB')
    influx_tea_user = config.get('Tea', 'USER')

    r = requests.post('https://{}:8086/write'.format(influx_tea_url),
        params = {  'u': influx_tea_user,
                    'p': influx_tea_pass,
                    'db': influx_tea_db,},
        data = 'tea,brewer={} count={}'.format(brewer.capitalize(), count))
    r.raise_for_status()
    assert r.status == 204, 'Write was unsuccessful'
    assert r.text == '', 'Write was unsuccessful'

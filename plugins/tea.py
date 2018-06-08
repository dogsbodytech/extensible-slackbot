import re
import traceback
import requests

def msg_contains_react_tea(message):
    try:
        brewer, count = re.match(r'(\w*) made (\w*) tea.*', message).group(1,2)
        post_tea_data(brewer, count)
        return 'realtea'
    except Exception as e1:
        try:
            print(traceback.format_exc(e1))
        except Exception as e2:
            # Python traceback bug, this will do
            print(e2)
        return 'fire'

def post_tea_data(brewer, count):
    config = configparser.ConfigParser()
    with open(r'config.txt') as f:
        config.readfp(f)

    influx_tea_url = config.get('TEA_URL')
    influx_tea_pass = config.get('TEA_KEY')
    influx_tea_db = config.get('TEA_DB')
    influx_tea_user = config.get('TEA_USER')

    requests.post('https://{}:8086/write'.format(influx_tea_url),
        data = {    'u': influx_tea_user,
                    'p': influx_tea_pass,
                    'db': influx_tea_db,
                    'brewer': brewer,
                    'count': count})


import requests

def at_bot_reply_get_random_quote(message):
    if not message.startswith('quote'):
        return "I'm sorry Dave, I'm afraid I can't do that."

    response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text').text
    return response

if __name__ == '__main__':
    print(get_random_quote())

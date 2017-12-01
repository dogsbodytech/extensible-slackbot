
import requests

def get_random_quote():
    response = requests.get('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text').text
    return response

if __name__ == '__main__':
    print(get_random_quote())


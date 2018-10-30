import re
def msg_contains_react_late(message):
    if not re.match(r'(?:^|.*\W)late(?:$|\W)', message):
        return
    return 'hushed'

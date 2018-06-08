import re
def msg_contains_react_late(message):
    if not re.match(r'late$', message) and not 'late ' in message:
        return
    return 'hushed'

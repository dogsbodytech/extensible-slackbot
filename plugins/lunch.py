import json
import random
import os

def msg_contains_react_lunch(message):
    reaction = 'pizza'
    return reaction

def msg_contains_reply_ocr_lunch(message):
    # Default reaction
    reaction = 'pizza'
    # Use the reactions file if it exists and contains data in the expected
    # format
    # The file is intended to be dynamic so we're just going to read it in again
    # everytime this funciton is called
    try:
        # Look for a json file containing a list of reactions
        with open(os.path.realpath(__file__).replace('.py', '.json')) as f:
            reactions = json.load(f)

        reaction = random.choice(reactions)
    except:
        pass

    return reaction

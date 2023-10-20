from dotenv import load_dotenv, find_dotenv
import os

def getenv(whatkey):
    load_dotenv(find_dotenv())

    what = os.getenv(whatkey)

    if what.lower() == 'true':
        return True
    elif what.lower() == 'false':
        return False
    else:
        return what
PRESENT_SYMBOL = "X"

def isPresentSymbol (myString):
        return myString.strip().upper() == PRESENT_SYMBOL

def isNotBlank (myString):
    '''
    Check if empty
    '''
    return bool(myString and myString.strip())

def parse_url_object_id(user_url):
    '''
    Parse meetup user id from url
    '''
    if( not user_url):
        return

    if(user_url[-1] == "/"):
        return user_url.split("/")[-2]
    else:
        return user_url.split("/")[-1]
        
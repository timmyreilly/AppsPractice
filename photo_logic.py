import urllib
from requests import request 

from tokens import COMPUTER_VISION_TOKEN


import urllib



def find_photo(url):
    try:
        urllib.urlretrieve(url, "static/photo.jpg")
    except:
        print "not a valid url"
        urllib.urlretrieve("http://i0.wp.com/timmyreilly.azurewebsites.net/wp-content/uploads/2016/07/wazzupdogimdex.png", "static/photo.jpg")

def get_photo_info(url):
    """Takes the URL of a photo and returns info from Cognitive Services about the image"""
    
    params = { 'visualFeatures' : 'Color,Categories'}
    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = COMPUTER_VISION_TOKEN
    headers['Content-Type'] = 'application/json'
    json = { 'url': url }
    data = None
    try: 
        result = processRequest( json, data, headers, params)
        return result
    except Exception as e:
        print "WELP"
        print e 
        return None 


    
def processRequest( json, data, headers, params ):
    _url = 'https://api.projectoxford.ai/vision/v1/analyses' 
    _maxNumRetries = 10
    retries = 0 
    result = None

    while True: 
        response = request( 'post', _url, json=json, data = data, headers = headers, params = params)
        if response.status_code == 429:
            print("Message: %s" % (response.json()['error']['message']))
            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1 
                continue 
            else:
                print ("Error: failed after retrying")

        elif response.status_code == 200 or response.status_code == 201: 
            if 'content-lenght' in response.headers and int(response.headers['content-lenght']) == 0:
                return None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content 
        else:
            print( "Error code: %d" % ( response.status_code ))
            print( "Message: %s" % (response.json()['error']['message']))
            return response 
        break 
    return result 
                

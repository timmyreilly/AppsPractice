from photo_logic import processRequest
from tokens import * 

urlImage = 'http://i0.wp.com/timmyreilly.azurewebsites.net/wp-content/uploads/2016/07/wazzupdogimdex.png'

params = { 'visualFeatures' : 'Color,Categories'}
headers = dict()
headers['Ocp-Apim-Subscription-Key'] = COMPUTER_VISION_TOKEN
headers['Content-Type'] = 'application/json'
json = { 'url': urlImage }
data = None

result = processRequest( json, data, headers, params )


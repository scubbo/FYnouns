import textwrap
import PIL
import base64
import urllib2 as urllib
import requests
import StringIO

#here's a comment, ladies and gentlemen

#####################
## TODOS
#
# - Caching
# - Prevent hotlinking (autoupload to imgur?)
#
#####################

def findImage(inputString):
	#search Google for the relevant image, and return it
    pass

if __name__ == '__main__':
	print 'You\'re totally reading this right now, aren\'t you?'

def doItAll(searchTerm, index=0, safeSearch=True):
    pass

def addTextToImage(originalImage, text):
    textToWrite = ["FUCK YEAH"] + textwrap.wrap(text.upper(), 70)
    #2nd argument of textwrap.wrap is the width - tweak this as needed.

def mar(searchTerm, index=0, safeSearch=True):
    return makeAuthorizedRequest(searchTerm, index, safeSearch)

def makeAuthorizedRequest(searchTerm, index=0, safeSearch=True):
    headerData = {'Authorization': 'Basic ' + auth}
    searchUri = makeSearchUri(searchTerm, safeSearch)
    urlRequest = requests.get(searchUri, headers=headerData)
    imageData = urlRequest.json()['d']['results'][index]
    imageHeight = imageData['Height'] #Unused
    imageWidth = imageData['Width'] #Unused
    imageUrl = imageData['MediaUrl']
    imageRequest = requests.get(imageUrl)
    image = PIL.Image.open(StringIO.StringIO(imageRequest.content))
    return image

def makeSearchUri(searchTerm, safeSearch=True):
    returnString = "https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&Query=%27" + urllib.quote(searchTerm) + "%27"
    if safeSearch:
        returnString += "&Adult=%27Strict%27"
    else:
        returnString += "&Adult=%27Off%27"
    return returnString

accountKey = "kMagMc7T2GKAh5gjIfEQFpP9x9I36SnzHvvcGhp2jU0="
auth = base64.encodestring("$acctKey:" + accountKey)

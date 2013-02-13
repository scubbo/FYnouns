import textwrap
import base64
import urllib2 as urllib
import requests
import StringIO
import os, os.path
from PIL import Image, ImageDraw, ImageFont

#####################
## TODOS
#
# - Caching (think I've done this, confirm)
# - Outlined text (think I've done this, confirm)
# - Prevent hotlinking (autoupload to imgur?)
# - add image at 'img/unfound.jpg'
# - indexError at :?? => nothing found
# - splitting the text into two lines if it is significantly longer than "FUCK YEAH"
# - set "fontpath" dynamically (package font up with app?)
# - put accountKey in a separate file
#
#####################

def findImage(inputString):
	#search Google for the relevant image, and return it
	pass

if __name__ == '__main__':
	print 'You\'re totally reading this right now, aren\'t you?'

def getURLToImage(searchTerm, selectionType='top', safeSearch=True):
	if selectionType=='top':
		#Always return the top result
		imgPath = makeImagePath(searchTerm, 0, safeSearch)
		if not os.path.exists(imgPath):
			makeNewImage(searchTerm, 0, safeSearch)
		return imgPath
	if selectionType=='random':
		#Pick a result at random
		cacheSafeNum = len(os.listdir('img/' + searchTerm.lower() + '/ss'))
		cacheUnsafeNum = len(os.listdir('img/' + searchTerm.lower() + '/us'))
		cacheNum = cacheSafeNum + cacheUnsafeNum
		if shouldRandomMakeNew(cachenum):
			if safeSearch:
				newIndex = cacheSafeNum
			else:
				newIndex = cacheUnsafeNum
			makeNewImage(searchTerm, newIndex, safeSearch)
			return makeImagePath(searchTerm, newIndex, safeSearch)
		else:
			if safeSearch:
				upperLimit = cacheSafeNum
			else:
				upperLimit = cacheUnsafeNum
			return makeImagePath(searchTerm, random.randrange(0, upperLimit), safeSearch)
	return 'img/unfound.jpg'

def makeImagePath(searchTerm, index, safeSearch):
	imgPath = 'img/'
	imgPath += searchTerm.lower() + '/'
	if safeSearch:
		imgPath += 'ss/'
	else:
		imgPath += 'us/'
	imgPath += str(index) + '.jpg'
	return imgPath
	

def makeNewImage(searchTerm, index=0, safeSearch=True):
	im = searchForAndSubtitleImage(searchTerm, index, safeSearch)
	savePath = makeImagePath(searchTerm, index, safeSearch)
	try:
		im.save(savePath, "JPEG")
	except IOError:
		os.makedirs(os.path.dirname(savePath))
		im.save(savePath, "JPEG")

def searchForAndSubtitleImage(searchTerm, index=0, safeSearch=True):
	im = getImageFromBing(searchTerm, index, safeSearch)
	addTextToImage(im, searchTerm)
	return im

def addTextToImage(image, text):
	text = text.upper() #this is VERY important :)
	dims = image.size
	
	fontsize = 1
	fontpath = "/Library/Fonts/Arial Rounded Bold.ttf"
	font = ImageFont.truetype(fontpath, fontsize)
	while (font.getsize("FUCK YEAH")[0] < dims[0] - 20) and (font.getsize(text)[0] < dims[0] - 20):
		fontsize += 1
		font = ImageFont.truetype(fontpath, fontsize)
	
	draw = ImageDraw.Draw(image)
	w1, h1 = draw.textsize("FUCK YEAH", font=font)
	w2, h2 = draw.textsize(text, font=font)
	top = dims[1] - (h1 + h2 + 10)
	drawOutlinedText(draw, ((dims[0] - w1)/2, top), "FUCK YEAH", font)
	drawOutlinedText(draw, ((dims[0] - w2)/2, top+h1), text, font)
	return image

def drawOutlinedText(draw, location, text, font, fill="white", outline="black", width=1)
	draw.text((location[0]-width, location[1]), text, outline, font)
	draw.text((location[0], location[1]-width), text, outline, font)
	draw.text((location[0]+width, location[1]), text, outline, font)
	draw.text((location[0], location[1]+width), text, outline, font)
	draw.text((location[0], location[1]), text, fill, font)
	
def getImageFromBing(searchTerm, index=0, safeSearch=True):
	headerData = {'Authorization': 'Basic ' + auth}
	searchUri = makeSearchUri(searchTerm, safeSearch)
	urlRequest = requests.get(searchUri, headers=headerData)
	try:
		imageData = urlRequest.json()['d']['results'][index]
		imageHeight = imageData['Height'] #Unused
		imageWidth = imageData['Width'] #Unused
		imageUrl = imageData['MediaUrl']
		imageRequest = requests.get(imageUrl)
		image = Image.open(StringIO.StringIO(imageRequest.content))
		return image
	except: #make this an explicit exception
		raise IOError("No Image found on Bing")

def makeSearchUri(searchTerm, safeSearch=True):
	returnString = "https://api.datamarket.azure.com/Bing/Search/v1/Image?$format=json&Query=%27" + urllib.quote(searchTerm) + "%27"
	if safeSearch:
		returnString += "&Adult=%27Strict%27"
	else:
		returnString += "&Adult=%27Off%27"
	return returnString

accountKey = "kMagMc7T2GKAh5gjIfEQFpP9x9I36SnzHvvcGhp2jU0="
auth = base64.encodestring("$acctKey:" + accountKey)

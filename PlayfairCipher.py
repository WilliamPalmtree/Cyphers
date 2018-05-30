import numpy as np
def getIndex(character):
	if (ord(character) > 64 and ord(character) < 91):
		character = chr(ord(character) + 32)
	if (ord(character) >= 106):
		character = chr(ord(character) - 1)
	character = ord(character)-97
	return character // 5, character % 5
def checkIfUsed(character,alphaArray):
	
	dex = getIndex(character)
	if(alphaArray[dex] == 0):
		alphaArray[dex] = 1
		return 0
	else:
		return 1
def keyGenerator(key):
	alphaArray = np.zeros((5,5,))
	key = key + "abcdefghiklmnopqrstuvwxyz"
	arX = 0
	arY = 0
	codeArray = [["","","","",""],["","","","",""],["","","","",""],["","","","",""],["","","","",""]]
	for ch in key:
		if (arX > 4):
			arX = arX - 5
			arY = arY + 1
		if(checkIfUsed(ch,alphaArray) == 0):
			print(arY)
			codeArray[arY][arX] = ch
			arX = arX + 1
	print(codeArray)
	return codeArray
def encodeMessage(message, key):
	print "hello"

keyGenerator("hello")
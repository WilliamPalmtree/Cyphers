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
	codeArray = np.empty((5,5,), dtype='a1')
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
def bimessage(message):
	l = len(message)
	if l % 2 == 1:
		message += 'x'

	out = []
	for n in range(0, len(message), 2):
		out.append(message[n:n+2])

	return out
	

def encodeMessage(message, key):
	keyA = keyGenerator(key)
	startEncode = bimessage(message)
	# for index in array?
	finishedEncode = ""

	print(keyA)
	for item in startEncode:
		index1, = zip(*np.where(keyA == item[0]))
		index2, = zip(*np.where(keyA == item[1]))
		i_final1 = None
		i_final2 = None
		if(index1[0] == index2[0]):
			i_final1 = ((index1[0] + 1)%5, index1[1])
			i_final2 = ((index2[0] + 1)%5, index2[1])
		if(index1[1] == index2[1]):
			i_final1 = (index1[0],(index1[1] + 1)%5)
			i_final2 = (index2[0],(index2[1] + 1)%5)
		else:
			i_final1 = (index2[0],index1[1])
			i_final2 = (index1[0],index2[1])
		letter1 = keyA[i_final1]
		letter2 = keyA[i_final2]
		finishedEncode = finishedEncode + letter1 + letter2
	return finishedEncode

def decodeMessage(message, key):
	keyA = keyGenerator(key)
	startDecode = bimessage(message)
	# for index in array?
	finishedDecode = ""

	print(keyA)
	for item in startDecode:
		index1, = zip(*np.where(keyA == item[0]))
		index2, = zip(*np.where(keyA == item[1]))
		i_final1 = None
		i_final2 = None
		if(index1[0] == index2[0]):
			if(index1[0] - 1 < 0 and index2[0] - 1 > 0):
				i_final1 = ((index1[0] + 4)%5, index1[1])
				i_final2 = ((index2[0] - 1)%5, index2[1])
			elif(index2[0] - 1 < 0 and index1[0] - 1 > 0):
				i_final2 = ((index2[0] + 4)%5, index2[1])
				i_final1 = ((index1[0] - 1)%5, index1[1])
			elif(index2[0] - 1 < 0 and index1[0] - 1 < 0):
				i_final1 = ((index1[0] + 4)%5, index1[1])
				i_final2 = ((index2[0] + 4)%5, index2[1])
			else:
				i_final1 = ((index1[0] - 1)%5, index1[1])
				i_final2 = ((index2[0] - 1)%5, index2[1])
		if(index1[1] == index2[1]):
			if(index1[1] - 1 < 0 and index2[1] - 1 > 0):
				i_final1 = ((index1[0]), index1[1] + 4)
				i_final2 = (index2[0],(index2[1] - 1)%5)
			elif(index2[1] - 1 < 0 and index1[1] - 1 > 0):
				i_final2 = ((index1[0]), index2[1] + 4)
				i_final1 = (index1[0],(index1[1] - 1)%5)
			elif(index2[1] - 1 < 0 and index1[1] - 1 < 0):
				i_final1 = ((index1[0], index1[1] + 4))
				i_final2 = ((index2[0], index2[1] + 4))
			else:
				i_final1 = (index1[0],(index1[1] - 1)%5)
				i_final2 = (index2[0],(index2[1] - 1)%5)
		else:
			i_final1 = (index2[0],index1[1])
			i_final2 = (index1[0],index2[1])
		letter1 = keyA[i_final1]
		letter2 = keyA[i_final2]
		finishedDecode = finishedDecode + letter1 + letter2
	return finishedDecode
print(encodeMessage("message", "hello"))
print(decodeMessage("lktthbwl", "hello"))
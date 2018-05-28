def letterSub(letter, key):
	
	if (ord(letter) < 123 and ord(letter) > 96):
	#Lowercase
		if (ord(letter) + key > 122):
			letter = chr(ord(letter) + key - 26)
		elif(ord(letter) + key < 97):
			letter = chr(ord(letter) + key + 26)
		else:
			letter = chr(ord(letter) + key)
	elif (ord(letter) > 64 and ord(letter) < 91):
		# Uppercase
		if (ord(letter) + key > 90):
			letter = chr(ord(letter) + key - 26)
		elif(ord(letter) + key < 65):
			letter = chr(ord(letter) + key + 26)
		else:
			letter = chr(ord(letter) + key)
	elif (ord(letter) < 65 and ord(letter) > 31):
		# symbols and numbers
		if (ord(letter) + key > 64):
			letter = chr(ord(letter) + key - 32)
		elif(ord(letter) + key < 32):
			letter = chr(ord(letter) + key + 32)
		else:
			letter = chr(ord(letter) + key)

	return letter

def encodeMessage(message, key):
	encodedMessage = ""
	vig = []
	vigNum = 0
	# this list will hold the ASCII values for the key
	for ch in key:
		if (ord(ch) < 123 and ord(ch) > 96):
			vig.append(ord(ch) - 96) # append the ith ASCII value from the key into the list vig[]
		elif (ord(ch) > 64 and ord(ch) < 91):
			vig.append(ord(ch) - 64)
		elif (ord(ch) < 65 and ord(ch) > 31):
			vig.append(ord(ch) - 31)


	for ch in message:

		if (vigNum > len(key) - 1):
			vigNum = vigNum - len(key)
			newEncodeLetter = letterSub(ch, vig[vigNum])
			print("1. SubKey: " + str(vig[vigNum]) + " Old: " + ch + " New: " + newEncodeLetter)
			encodedMessage = encodedMessage + newEncodeLetter
			vigNum = vigNum + 1
		else:
			newEncodeLetter = letterSub(ch, vig[vigNum])
			print("2. SubKey: " + str(vig[vigNum]) + " Old: " + ch + " New: " + newEncodeLetter)
			encodedMessage = encodedMessage + newEncodeLetter
			vigNum = vigNum + 1
	return(encodedMessage)
	print(encodedMessage)

def decodeMessage(message, key):
	decodedMessage = ""
	vig = []
	vigNum = 0
		# this list will hold the ASCII values for the key
	for ch in key:
		if (ord(ch) < 123 and ord(ch) > 96):
			vig.append(ord(ch) * -1 + 96) # append the ith ASCII value from the key into the list vig[]
		elif (ord(ch) > 64 and ord(ch) < 91):
			vig.append(ord(ch) * -1 + 64)
		elif (ord(ch) < 65 and ord(ch) > 31):
			vig.append(ord(ch) * -1 + 31)

	for ch in message:
		if (vigNum > len(key) - 1):
			vigNum = vigNum - len(key)
			newDecodeLetter = letterSub(ch, (vig[vigNum]))
			print("1. SubKey: " + str(vig[vigNum]) + " Old: " + ch + " New: " + newDecodeLetter)
			decodedMessage = decodedMessage + newDecodeLetter
			vigNum = vigNum + 1
		else:
			newDecodeLetter = letterSub(ch, (vig[vigNum]))
			print("2. SubKey: " + str(vig[vigNum]) + " Old: " + ch + " New: " + newDecodeLetter)
			decodedMessage = decodedMessage + newDecodeLetter
			vigNum = vigNum + 1
	return(decodedMessage)
	print(decodedMessage)
key = raw_input("Please input a word or phrase key: ")
print("Your key is " + str(key))
message = raw_input("Now please type your message: ")
ED = raw_input("Would you like to encode or decode? Please use E or D ")
if(ED == "E"):
	print(encodeMessage(message, key))
if(ED == "D"):
	print(decodeMessage(message, key))
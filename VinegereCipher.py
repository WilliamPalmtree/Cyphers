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
			vig.append(ord(ch)-31)


	for ch in message:
		if (vigNum > 6):
			vigNum - 6
			newEncodeLetter = letterSub(ch, vig[vigNum])
			encodedMessage = encodedMessage + newEncodeLetter
			vigNum + 1
		else:
			newEncodeLetter = letterSub(ch, vig[vigNum])
			encodedMessage = encodedMessage + newEncodeLetter
			vigNum + 1
	return(encodedMessage)
	print(encodedMessage)

message = "Hello and good morning to you and your kin"
print(encodeMessage(message,"Good morning"))

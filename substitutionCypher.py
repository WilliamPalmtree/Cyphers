# LetterSub takes a character and a key and returns a character
# shifted by the key amount
def letterSub(letter, key):
	key = key % 26
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

# Encode messages takes the message and the key value and returns 
# the encoded string
def encodeMessage(message, key):
	encodedMessage = ""
	for ch in message:
		newEncodeLetter = letterSub(ch, key)
		encodedMessage = encodedMessage + newEncodeLetter
	return(encodedMessage)
	print(encodedMessage)

# Decode message takes the message and the key value and returns 
# the original string
def decodeMessage(encodedMessage, key):
	decodedMessage = ""
	for ch in message:
		newDecodeLetter = letterSub(ch, -key)
		decodedMessage = decodedMessage + newDecodeLetter
	print(decodedMessage)
key = input("Please input a number key: ")
print("Your key is " + str(key))
message = raw_input("Now please type your message: ")
ED = raw_input("Would you like to encode or decode? ")
if(ED == "encode"):
	print(encodeMessage(message, key))
if(ED == "decode"):
	print(decodeMessage(message, key))

# LetterSub takes a character and a key and returns a character
# shifted by the key amount
def letterSub(letter, key):

	if (ord(letter) + key > 122):
		letter = chr(ord(letter) + key - 26)
	else:
		letter = chr(ord(letter) + key)
	return letter

# Encode messages takes the message and the key value and returns 
# the encoded string
def encodeMessage(message, key):
	encodedMessage = ""
	for ch in message:
		newLetter = letterSub(ch, key)
		encodedMessage = encodedMessage + newLetter
	print(encodedMessage)
# key = input("Please input a number key ")
# key = 13
# print("Your key is" + str(key))
# message = input("Now please type your message:")
message = "thisismyawesomeencodedmessage"
# letter = character 1 of message
letter = "t"
encodeMessage(message, 12)
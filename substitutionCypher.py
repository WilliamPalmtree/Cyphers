# LetterSub takes a character and a key and returns a character
# shifted by the key amount
def letterSub(letter, key):

	if (ord(letter) + key > 122):
		print(ord(letter)+key)
		letter = chr(ord(letter) + key - 26)
	else:
		letter = chr(ord(letter) + key)
		print(ord(letter)+key)
	print(letter)


# Encode messages takes the message and the key value and returns 
# the encoded string
def encodeMessage(message, key):

# key = input("Please input a number key ")
# key = 13
# print("Your key is" + str(key))
# message = input("Now please type your message:")
message = "this is my awesome encoded message"
# letter = character 1 of message
letter = "t"
letterSub(message,12)

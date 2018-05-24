def letterSub(letter, key):

	if (ord(letter) + key > 122):
		print(ord(letter)+key)
		letter = chr(ord(letter) + key - 26)
	else:
		letter = chr(ord(letter) + key)
		print(ord(letter)+key)
	print(letter)
# key = input("Please input a number key ")
# key = 13
# print("Your key is" + str(key))
# message = input("Now please type your message:")
message = "this is my awesome encoded message"
# letter = character 1 of message
letter = "t"
letterSub(letter,12)

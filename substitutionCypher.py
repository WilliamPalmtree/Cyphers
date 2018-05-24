def letterSub(str, key):
	for ch in str:
		if (ord(ch) + key > 122):
			print(ord(ch)+key)
			str = chr(ord(ch) + key - 26)
		else:
			str = chr(ord(ch) + key)
			print(ord(ch)+key)
	print(str)
# key = input("Please input a number key ")
# key = 13
# print("Your key is" + str(key))
# message = input("Now please type your message:")
message = "this is my awesome encoded message"
# letter = character 1 of message
letter = "t"
letterSub(message,12)

input_string=raw_input("Enter a list of words seprated by spaces:")
words=input_string.split()
longest_word=""
longest_length=0
for word in words:
	if len(word)>longest_length:
		longest_length=len(word)
		longest_word=word
print "length of the longest word:",longest_length
print "The largest word is:",longest_word

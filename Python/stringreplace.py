input_string=raw_input("Enter a string :")
if input_string:
 first_char=input_string[0]
 modified_string=first_char+input_string[1:].replace(first_char,"$")
 print "Modified string :",modified_string
else:
 print "Empty string provided"

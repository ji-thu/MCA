input_string=raw_input("Enter a string:")
if input_string.endswith("ing"):
 result_string=input_string+"ly"
else:
 result_string=input_string+"ing"
print "resulting string:",result_string

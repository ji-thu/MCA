input_string=raw_input("enter string:")
if len(input_string)>1:
 modified_string =input_string[-1]+ input_string [1:-1] + input_string[0]
else:
 modified_string= input_string;
print("modified string:", modified_string)

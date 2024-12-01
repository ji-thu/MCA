filename=raw_input("Enter the file name:")
if "." in filename:
 extension=filename.split(".")[-1]
 print "The extension of the file is:",extension
else:
 print "The file has no extension"

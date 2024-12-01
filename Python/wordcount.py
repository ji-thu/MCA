line=raw_input("enter a line of text :")
words=line.lower().split()
word_count={}
for word in words:
 if word in word_count:
  word_count[word]+=1
 else:
  word_count[word]=1
print"word occurences:"
for word,count in word_count.items():
 print"{0}:{1}".format(word,count)

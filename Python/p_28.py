try:
 n=int(raw_input("Enter the number of steps(N):"))
 for i in range(1,n+1):
  raw=[]
  for j in range(1,i+1):
   raw.append(i*j)
  print " ".join(map(str,raw))
except ValueError:
 print "Please enter a valid integer"

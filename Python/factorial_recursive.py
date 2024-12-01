def factorial_recursive(n):
 if n==0 or n==1:
  return 1 
 else:
  return n* factorial_recursive(n-1)
num= int(raw_input("enter a number:"))
result=factorial_recursive(num)
print "the factorial of" ,num, "is" ,result
 

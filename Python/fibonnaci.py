def fibonnaci_iterative(n):
 fib_series=[]
 a,b=0,1
 for i in range (n):
  fib_series.append(a)
  a,b=b, a+b
 return fib_series
num_terms=int(raw_input("enter the number of terms for the fibonnaci series:"))
result=fibonnaci_iterative(num_terms)
print "the fibonnaci series for",num_terms, "terms is:",result

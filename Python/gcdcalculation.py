def find_gcd(num1, num2):
 while num2:
  num1, num2=num2,num1% num2
 return num1
number_1=56
number_2=98
gcd=find_gcd(number_1, number_2)
print"the GCD of ",number_1," and ",number_2," is: ",gcd

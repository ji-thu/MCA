def swap_and_merge(str1,str2):
 if len(str1)<2 or len(str2)<2:
  return "Both strings must have at least 2 characters"
 new_str1=str1[0]+str2[1]+str1[2:]
 new_str2=str2[0]+str1[1]+str2[2:]
 result=new_str1+" "+new_str2
 return result
string1=raw_input("Enter the first string:")
string2=raw_input("Enter the second string:")
result=swap_and_merge(string1,string2)
print result

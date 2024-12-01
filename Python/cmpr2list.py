list_1=list(map(int, raw_input("enter the first of integers(space-seperated):").split()))
list_2=list(map(int, raw_input("enter the second of integers(space-seperated):").split()))
same_length=len (list_1)==len (list_2)
same_sum= sum(list_1)==sum (list_2)
common_values= set (list_1) & set (list_2)
print "a) Are the lists of the same length;",same_length
print "b) Do thr list sum to the same value;",same_sum
print "c) Do any values occur in both lists;",bool(common_values)
if common_values:
 print "common values:", common_values

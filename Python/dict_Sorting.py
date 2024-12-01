my_dict = {'apple': 4, 'banana': 2, 'orange': 5, 'mango': 3}
sorted_dict_asc = dict(sorted(my_dict.items()))
print "Sorted by keys (ascending):", sorted_dict_asc
sorted_dict_desc = dict(sorted(my_dict.items(), reverse=True))
print "Sorted by keys (descending):", sorted_dict_desc

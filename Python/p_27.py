def count_character_frequency(input_string):
    frequency = {} 
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1 
        else:
            frequency[char] = 1  
    
    return frequency


user_input = raw_input("Enter a string: ")
result = count_character_frequency(user_input)


print("Character frequency:")
for char, count in result.items():
    print char, ":", count

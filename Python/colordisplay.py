input_colors = raw_input("Enter color names separated by commas: ")

color_list = [color.strip() for color in input_colors.split(',')]

if input_colors:  
    first_color = color_list[0]
    last_color = color_list[-1]
    print "First color:", first_color
    print "Last color:", last_color
else:
    print "No colors entered."

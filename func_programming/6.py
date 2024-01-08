colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

convert_to_string = lambda color_tuple: ' '.join(color_tuple)

result = list(map(convert_to_string, colors))

print(result)

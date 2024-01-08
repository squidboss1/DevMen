original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square_function = lambda x: x ** 2

cube_function = lambda x: x ** 3

squares = list(map(square_function, original_list))
cubes = list(map(cube_function, original_list))

print("Oryginalna lista:")
print(original_list)

print("\nKwadraty liczb:")
print(squares)

print("\nSześciany liczb:")
print(cubes)

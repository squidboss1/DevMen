nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_nums = list(filter(lambda x: x % 2 == 0, nums))
new_nums = list(map(lambda x: x ** 2, filtered_nums))

print(new_nums)
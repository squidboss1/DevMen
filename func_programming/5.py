from functools import reduce

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]

sum_of_each_num = lambda x, y: [x[i] + y[i] for i in range(len(x))]

sum_of_nums = sum(reduce(sum_of_each_num, [nums1, nums2, nums3]))

print(sum_of_nums)

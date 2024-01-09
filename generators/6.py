three_d = [
    [[1, 2, 3, 4],
     [0, -1, -2, -3, -4, -5, -6]],
    [[1, 10, 15, 12, 20, 20, 20],
     [-15, -13, 14, 20, -1]]
]

filtered_lists = [inner_list
                  for outer_list in three_d
                  for inner_list in outer_list
                  if len(inner_list) > 4
                  ]

print(filtered_lists)

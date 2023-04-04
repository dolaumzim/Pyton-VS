margin = 50
gap = 30
gap_group = 50

n_group_rows = 3
n_group_columns = 3

n_input_rows = 3
n_input_columns = 3

groups = []

for group_row in range(n_group_rows):
    for group_column in range(n_group_columns):
        group = []
        
        for input_row in range(n_input_rows):
            for input_column in range(n_input_columns):
                group.append(f'{input_row + 1} - {input_column + 1}')
        
        groups.append(group)

print(groups)

#  |  |  |
# [2, 5, 0, 0, 3, 0, 9, 0, 1],
# [0, 1, 0, 0, 0, 4, 0, 0, 0],
# [4, 0, 7, 0, 0, 0, 2, 0, 8],
#  |  |  |
# [0, 0, 5, 2, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 9, 8, 1, 0, 0],
# [0, 4, 0, 0, 0, 3, 0, 0, 0],
#  |  |  |
# [0, 0, 0, 3, 6, 0, 0, 7, 2],
# [0, 7, 0, 0, 0, 0, 0, 0, 3],
# [9, 0, 3, 0, 0, 0, 6, 0, 4]

original_list = [1, 2, 2, 3, 4, 4, 5,5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(f'Hard way: {unique_list}')

temp = list(set(unique_list))

print(f'SOFT way: {temp}')


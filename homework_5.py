

# დავალება 1

# num_list = [5, 19, 21, 37, 12]

# sum = 0
# count = 0

# for num in num_list:
#     sum += num
#     count += 1

# average = sum / count

# print(f'Total sum is {sum}, and average - {average}.' )




# # დავალება 2

# given_list = ['a', 'b', 2, 4, 2, 'c', 'j', 1, 'b', 'd', 'c', 4, 1]
# unique_list = []

# for elem in given_list:
  
#     if elem not in unique_list:
#         unique_list.append(elem)

# print(unique_list)




# #დავალება 3

# from random import randint

# my_list = [randint(-50, 50) for _ in range(20)]

# even_list =[]

# for num in my_list:
#     if num % 2 == 0:
#         even_list.append(num)

# print(my_list)
# print(f'\neven numbers list: {even_list}' )


# დავალება 4



long_names_list = []
short_name_list = []

while True:
    
    user_name = input('Please enter name: ')

    strip_name = user_name.strip()

    if strip_name.lower() in["stop", "exit", "quit"]:
        print('Program ended.')
        break

    capitalize_name = strip_name.capitalize()

    if len(capitalize_name) > 3:
        long_names_list.append(capitalize_name)
    else:
        short_name_list.append(capitalize_name)


print(f'Long names list: {long_names_list}')
print(f'\nShort names list: {short_name_list}')
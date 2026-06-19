# დავალება 1

# my_dict = {key : key ** 2 for key in range(1,11)}

# print(my_dict)

# ___________________________________________________________

# დავალება 2

# products = [
#     {"cola": {"price": 1.5, "quantity": 10}},
#     {"fanta": {"price": 2.5, "quantity": 5}},
#     {"snickers": {"price": 3.5, "quantity": 12}},
#     {"water": {"price": 4.5, "quantity": 8}},
#     {"beer": {"price": 6.5, "quantity": 5}}
# ]

# print('Product names: ')
# for item in products:
   
#     product_name = list(item.keys())[0]
#     print(f"{product_name}")

# sum = 0

# for item in products:
#     for product_name, data in item.items():
      
#         product_total = data["price"] * data["quantity"]
#         sum += product_total

# print(f"Total sum of every product price is {sum}.")


# ________________________________________________________________

# დავალება 3

fruit_dict = {}

while True:
    user_input = input('Enter your favorite fruit: ')
    if user_input == 'stop':
        break
    else:
        if user_input in fruit_dict:
            fruit_dict[user_input] += 1
        else:
            fruit_dict[user_input] = 1

print(fruit_dict)





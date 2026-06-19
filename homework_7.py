# 1. მოცემულია სია:

# (სახელი, გვარი, ასაკი)

# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33), 
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
# while True:
    
#     user_name = input('Please enter your name: ')
    
#     valid_names = [person[0] for person in persons]

#     if user_name.lower() == 'stop':
#         break
#     elif user_name not in valid_names:
#         print('Name is not valid')
#         continue
    
#     user_surname = input('Now enter your surname: ')
    
#     if user_surname.lower() == 'stop':
#         break

#     valid_person = None

#     for person in persons:
#         if user_name == person[0] and user_surname == person[1]:
#             valid_person = person
#             continue

#     if valid_person:
#         print(f'Age is - {valid_person[2]}')
        
#     else:
#         print('Surname is not valid ')
        




# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)

word_1 = input('Please enter first word: ')
word_2 = input('Now enter second word: ')

set_1 = set(word_1)
set_2 = set(word_2)

common_symbols = set_1 & set_2

diff_symbols = set_1 ^ set_2

combined_symbols = set_1 | set_2

print(f'Common symbols are : {common_symbols}')
print(f'Different symbols : {diff_symbols}')
print(f'combined symbols : {combined_symbols}')
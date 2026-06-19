# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს, შემდეგ გვარს და რაიმე ფაილში ჩაწერს 
#    სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით, ყველა ახალი სახელი და გვარი უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
   
#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop

#    ფაილში უნდა ჩაიწეროს შემდეგი სახით:
#    1. Otar Tumanishvili
#    2. Nika Papaskiri

#    პროგრამა ჩერდება იმ შემთხევაში, თუ მომხმარებელმა სახელის ადგილას შეიყვანა სიტყვა stop

counter = 1
with open("persons11.txt", "w",) as file:
    while True:
        user_frstname = input('Enter your first name: ')
        if user_frstname.lower() == 'stop':
            print('program ended')
            break
    
        user_lstname = input('Enter your last name: ')
    
        file.write(f'{counter}. {user_frstname} {user_lstname}\n')
    
        counter += 1    

    
# ___________________________________________________

# 2. თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:
#    სახელი და გვარი, ასაკი, ქალაქი

#    Evelyn Cook, 75, Nixonland
#    Dr. Briana Davidson, 22, South Hunterside
#    ...
#    ...

#    თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
#    ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
#    ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!

# with open('persons.txt', 'r') as file:
#     for row in file:
#         parts = row.split(',')
#         age = int(parts[1].strip())

    
#         if age < 50:
#             with open('Persons_less50.txt', 'a') as less_file:
#                 less_file.write(row)
#         else:
#             with open('persons_more50.txt', 'a') as more_file:
#                 more_file.write(row)    
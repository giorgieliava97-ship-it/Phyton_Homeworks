# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს 
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის 
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:

#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30

#    და ა.შ.
   
#    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!

import csv

def datasaver(num):
    headers = ['ID','first_name','last_name','age']
    
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
    
    with open('users.csv', 'a', newline='') as file:
        dict_writer = csv.DictWriter(file, fieldnames=headers)
        
        for i in range(1, num+1):
            first_name = input('Enter first name: ')
            last_name = input('Enter last name: ')
            
            while True:
                try:
                    age = int(input('Enter age: '))
                    break
                except ValueError:
                    print('Please use numbers only!')

            dict_writer.writerow({
                "ID": i,
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            })

datasaver(5)

# _______________________________________________________________________


# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)

#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!

# import csv

# with open('students.csv', 'r', newline='') as main_file:
    
#     reader = csv.DictReader(main_file)
#     headers = ['ID','First Name','Last Name','Grade']

#     with open('failed_students.csv', 'w', newline='') as failed_file:
#         failed_writer = csv.DictWriter(failed_file, fieldnames=headers)
#         failed_writer.writeheader()
        
#         with open('passed_students.csv', 'w', newline='') as passed_file:
#             passed_writer = csv.DictWriter(passed_file, fieldnames=headers)
#             passed_writer.writeheader()

#             for row in reader:
#                 grade = int(row['Grade'])
        
#                 if grade < 50:
#                     failed_writer.writerow(row)

#                 else:
#                     passed_writer.writerow(row)
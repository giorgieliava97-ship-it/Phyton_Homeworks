# მოცემულია persons.json ფაილი შემდეგი სტრუქტურით:
        
# თქვენი დავალებაა დაწეროთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და გადაცემული რიცხვის საფუძველზე 
# იმდენჯერ ჰკითხავს მომხმარებელს სახელს და ასაკს, შემდეგ კი persons.json ფაილში დაამატებს ახალ პერსონებს
# თავისივე აიდებით.მაგალითათ ორჯერ ვეკითხებით მომხმარებელს:

# enter your name: Walter
# enter your age: 45
# enter your name: Niko
# enter your age: 32
# გაითვალისწინეთ! არ უნდა დაირღვეს json ფაილის სტრუქტურა, ანუ პერსონები უნდა იყოს ლისტში, ლისტის გარეთ არ ჩაამატოთ!
# ასევე, აიდები უნდა გაგრძელდეს ბოლო აიდის მქონე პერსონის შემდეგ ლოგიკურად, ანუ json ფაილში თუ ბოლო პერსონის აიდი იქნება 2, 
# ახალი პერსონის დამატებისას აიდი უნდა იყოს 3, თუ ბოლო პერსონის აიდი იქნება 5, ახალი პერსონის უნდა იყოს 6 და ასე შემდეგ!

import json

def persons_data(num):
    
    with open("persons.json", "r") as file:
            inserted_persons = json.load(file)
   
    if inserted_persons:
        next_id = inserted_persons[-1]["id"] + 1
    else:
        next_id = 1

    
    while num > 0:
        user_name = input("enter your name: ")
        user_age = int(input("enter your age: "))
        
        new_person = {
            "id": next_id,
            "name": user_name,
            "age": user_age
        }
        
        inserted_persons.append(new_person)
        
        next_id += 1
        num -= 1

    with open("persons.json", "w") as file:
        json.dump(inserted_persons, file, indent=4)


persons_data(3)
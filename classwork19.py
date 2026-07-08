# nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# new_list = [str(num) for num in nums_list]
#
# nums = ", ".join(new_list)

# print(nums)

# with open("nums.txt", "w") as file:
#     file.write(nums)

# with open("nums.txt", "r") as file:
#     data = file.read()
#
# my_list = data.split(", ")
#
# nums_list = [int(char) for char in my_list]
#
# print(nums_list)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: ({self.name}, {self.age})"

p1 = Person("Otar", 35)

def person_serializer(obj):

    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age
        }

    return f"{obj} is not a Person object"

# serialized_person = person_serializer(p1)


def person_deserializer(obj):
    if isinstance(obj, dict):
        return Person(obj["name"], obj["age"])

    return f"{obj} is not a dict"


# person = person_deserializer(serialized_person)

 

# გვაქვს შემდეგი კლასი და ინსტანსი:


# დაწერეთ სერიალაიზერ ფუნქცია, რომელიც დაგეხმარებათ არსებული კლასის ობიექტი გადააქციოთ ისეთ ობიექტად,
# რომ შემდეგ ტექსტურ ფაილში ჩაწეროთ შემდეგი სტრუქტურით:
# Name: Otar, Age: 35

# რათქმაუნდა ჩაწერეთ ფაილში.

# არსებული ფაილიდან წაიკითხეთ ინფორმაცია.

# ასევე დაწერეთ დესერიალაიზერ ფუნქცია, რომელიც ზემოაღნიშნული სტრუქტურის ფაილიდან წაკითხულ ინფორმაციას აქცევს ისევ 
# Person კლასის ობიექტად.(ჩათვალეთ რომ მხოლოდ ერთ ხაზს წერთ ფაილში და წაკითხვითაც ერთ ხაზს კითხულობთ)

file_name = "person_data.txt"


serialized_dict = person_serializer(p1)


text_to_save = f"Name: {serialized_dict['name']}, Age: {serialized_dict['age']}"


with open(file_name, "w") as file:
    file.write(text_to_save)

with open(file_name, "r") as file:
    file_content = file.readline().strip()



parts = file_content.split(", ")
name = parts[0].split(":")[1].strip()
age = int(parts[1].split(":")[1].strip())

dict_for_deserializer = {"name": name, "age": age}

person = person_deserializer(dict_for_deserializer)


print(person)  
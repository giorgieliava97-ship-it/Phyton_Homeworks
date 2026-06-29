
# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, 
# დაუწერეთ დეკორატორი,რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და 
# თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი

# def tax(func):
#     def wrapper(balance, payment):
#         balance -= 1
#         if balance < payment:
#             return f'There is not enough money!'
#         return func(balance, payment)
#     return wrapper

# @tax
# def transaction(balance, payment):
#         balance -= payment
#         return f'Payment complete, {balance} left on balance'

# print(transaction(11, 50))


#  2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს 
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!


class MyMeta(type):
    def __new__(mcls, name, bases, attrs):
        for attr_name, attr_value in attrs.items():
            if callable(attr_value):
                if not attr_name.startswith('_'):
                    raise ValueError(f"Method name '{attr_name}' is not valid. It should be starting with '_'")



        return super().__new__(mcls, name, bases, attrs)
        


class ValidClass(metaclass=MyMeta):
    
    def _test(self):
        pass
    

class InvalidClass(metaclass=MyMeta):
    def test(self):
        pass

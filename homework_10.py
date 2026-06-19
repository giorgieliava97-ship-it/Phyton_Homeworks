#1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#   [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით

my_list =  [(1, 3), (4, 2), (2, 5)]
print(sorted(my_list, key=lambda x: x[1]))
# _________________________________________________________

#2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს, 
#დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ 
#შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)
 
#def division(a, b):
#       return a / b
#try:     
#             a = int(input('please enter first number: '))
#             b = int(input('please enter second number: '))
#             result = division(a, b)
#             print(result)
#            
#except ValueError:
#	print('entering text not allowed')

#except ZeroDivisionError:
#	print('Can not be divided by zero')

#else:
#	print('No Error')
#	
#finally:
#	print('program ended')
	
# _________________________________________________________

#3. მოცემულია პროდუქტების ლისტი:

products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Mouse", "price": 15},
    {"name": "Keyboard", "price": 25},
    {"name": "Monitor", "price": 150},
    {"name": "Power", "price": 100},
    {"name": "Pad", "price": 10},
]

#filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;

# print(list(filter(lambda x: x['price']<100, products)))

# #map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი

# result = list(map(lambda x: (x['name'], x['price']), products))
# print(result)

# #sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით

# result = sorted(products, key=lambda x: x['price'])
# print(result)

# #reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

# from functools import reduce

# result = reduce(lambda x, y: x + y['price'], products, 0)

# print(result)

# _________________________________________________________

#4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს

# def sumtorial(n):
#     if n <= 0:
#         return 0

#     return n + sumtorial(n-1)
    

# print(sumtorial(10))
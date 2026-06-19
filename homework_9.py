# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის 
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი


# def numtotal(request_number=5):
#     total_sum = 0
#     for i in range(request_number):
#         user_number = int(input('Please enter a number: '))
#         total_sum += user_number
#     return total_sum

# print(numtotal())


# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

# def intsorter(*args):
#     even_list = []
#     odd_list = []

#     for num in args:
#         if num % 2 == 0:
#             even_list.append(num)
#         else:   
#             odd_list.append(num)
    
#     return even_list, odd_list

# even, odd = intsorter(1,2,3,4,5,6)

# print(even)
# print(odd)




# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

def wordcounter(text):
    
    word_dict = {}

    clean_text = text.replace('.', '').lower()
    words = clean_text.split()
    
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    
    return word_dict
        

print(wordcounter('This is a test. This test is fun.'))




# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო 
# იყო მაღალ რეგისტრში შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, 
# მომხმარებელმა თუ შეიყვანა ტექსტი Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ასოა ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.


# def uppercustom():
#     user_text = input('Please enter text: ')
#     uppercase_count = sum(1 for letter in user_text if letter.isupper())
#     return uppercase_count, user_text.upper()

# count, text = uppercustom()

# print(f'Total number of uppercase letter(s) are : {count}')
# print(f'Capitalized text: " {text} " ')    


# 
# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.

def snaked(cammel_text):
    result = ""
    
    for letter in cammel_text:
    
        if letter.isupper():
            result += '_' + letter.lower()
        else:
            result += letter
    return result

print(snaked('enterAnyCamelCase'))
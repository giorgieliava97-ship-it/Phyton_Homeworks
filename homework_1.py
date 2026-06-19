# დავალება ა

Cathet1 = int(input('Please enter the length of the first Cathet: '))
Cathet2 = int(input('Please enter the length of the Second Cathet: '))

Area = int(Cathet1 * Cathet2 / 2)
Hypothenuse = (Cathet1 ** 2 + Cathet2 ** 2) ** 0.5

print("Area of the triangle is ", Area)
print("Hypothenuse is ", Hypothenuse)

# ______________________________________________________
# დავალება ბ

Number_of_seconds = int(input('გთხოვთ მიუთითოთ წამების რაოდენობა: '))

# Second = int(Number_of_seconds % 60)
# Minute = int(Number_of_seconds / 60)
# Hour = int(Minute / 60)
# Day = int(Hour / 24)
# Week = int(Day / 7)
# Year = int(Day / 365)

Second = Number_of_seconds % 60
Minute = int(Number_of_seconds / 60) % 60
Hour = int(Number_of_seconds / 3600) % 24
Day = int(Number_of_seconds / 86400) % 365
Year = int(Number_of_seconds / 31536000)

print(Number_of_seconds, 'წამი არის', end=' ')

if Year != 0:
    print(Year, 'წელი', end=' ')

if Day != 0:
    print(Day, 'დღე', end=' ')

if Hour != 0:
    print(Hour, 'საათი', end=' ')

if Minute != 0:
    print(Minute, 'წუთი და', end=' ')

if Second != 0:
    print(Second, 'წამი')


# print( Year, 'year', Week, 'week', Day, 'day', Hour, 'hour', Minute, 'minute', Second, 'second')

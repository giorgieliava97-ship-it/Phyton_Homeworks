# დავალება#1

# sentence = input("Please enter the sentence: ")

# first_word = input("Enter first word: ")

# second_word = input("Enter second word: ")

# changed_sentence = sentence.replace(first_word, second_word)

# print(f"changed sentence: {changed_sentence} ")


# დავალება#2

# sentence = input("Please enter sentence: ")

# word_list = sentence.split()

# longest_word = word_list[0]

# for word in word_list:
#     if len(word) > len(longest_word):
#         longest_word = word

# print(f"The longest word in the sentecne is: {longest_word}")
  

# დავალება#3

word_1 = input("Please enter first word: ").lower()
word_2 = input("Enter second word: ").lower()

if len(word_1) != len(word_2):
    print("those words are not Anagrams")
else:
   
    for letter in word_1:

        word_2 = word_2.replace(letter, "", 1)
    
    if word_2 == "":
        print("those words are Anagrams")
    else:
        print("those words are not Anagrams.")



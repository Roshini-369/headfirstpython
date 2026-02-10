
vowels = ['a','e','i','o','u']
word = input("Enter a word to search for vowels:")
found = []
for letter in word:
    if letter in vowels:
       # print("letter in vowels",letter)
        if letter not in found:
            found.append(letter)
            #print("letter not in found",letter)
for vowel in found:
    print("vowel found",vowel)
print(list(found))
# Program to count the number of vowels in a string
word = input('enter any word ').lower()
vowel = ('a', 'e', 'i', 'o', 'u')
count = 0
for i in word:
    if i in vowel:
        count += 1
print("Number of vowels: ",count)
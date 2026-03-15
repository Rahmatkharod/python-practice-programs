# Program to check whether a string is a palindrome
# Ignores spaces and case differences

word = input('enter string to check for palindrom').lower().replace(" ", "" )
reverse = word[::-1]
if word == reverse:
    print(f'{word} is palindrome')
else:
    print(f'{word} is not palindrome') 
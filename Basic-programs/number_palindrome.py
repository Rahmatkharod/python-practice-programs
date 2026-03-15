# Program to check whether a number is a palindrome
num = int(input('enter number'))
# Check for negative numbers first
if num < 0:
    print("Negative numbers cannot be palindrome")
else:
    original_num = num
    rev = 0
    # Reverse the number
    while num > 0:
        digit =  num % 10 
        rev = rev *10 + digit
        num = num // 10
    print(rev)

    # Check if original number and reversed number are same
    if rev == original_num:
        print("palindrome")
    else:
        print("not palindrome")
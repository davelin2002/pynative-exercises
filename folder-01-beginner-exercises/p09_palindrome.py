# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. 
# A palindrome number reads the same forwards and backward. 
# For example, 545 is a palindrome number.

def check_palindrome(num):
    characters = list(str(num))
    isPalindrome = True

    left_index = 0
    right_index = len(characters) - 1
    while left_index <= right_index:
        if characters[left_index] == characters[right_index]:
            left_index += 1
            right_index -=1
        else:
            isPalindrome = False
            left_index += 1
            right_index -=1
    
    return isPalindrome

def main():
    print(check_palindrome(1))
    print(check_palindrome(121))
    print(check_palindrome(1221))
    print(check_palindrome(1223))

if __name__=="__main__":
    main()
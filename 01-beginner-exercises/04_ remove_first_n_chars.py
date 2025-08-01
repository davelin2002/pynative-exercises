# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove_chars(word, n):
    if (len(word) <= n) or (len(word) < 0):
        return "please enter a smaller number"
    else:
        return word[n:]

def main():

    print("Removing characters from a string")
    print(remove_chars("pynative", 4))
    # output 'tive' first four characters are removed

    print(remove_chars("pynative", 2)) 
    # output 'native'

    print(remove_chars("pynative", 8)) 
    # n is greater than the length of the word so an error is raised
if __name__ == "__main__":
    main()
# Exercise 3: Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

# initial attempt

def print_even_index_1():
    word = input("enter a word:")
    for i in range(0,len(word),2):
        print(word[i])

# attempting the problem with string slicing
def print_even_index_2():
    word = input("enter a word:")

    # easier to iterate over a list

    word_list = list(word)

    for letter in word_list[::2]:
        print(letter)

def main():
    print("output from standard and list slicing implementations:")
    print_even_index_1()
    print_even_index_2()

if __name__ == "__main__":
    main()
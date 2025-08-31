# Exercise 7: Find the number of occurrences of a substring in a string
# Write code to find how often the substring “Emma” appears in the given string.

# simplest implementation using the string method
# simply using the count method in order to count the number of times the word appears

def has_substring(word_string):
    num_appearances = word_string.count("Emma")
    return f"Emma has appeared {num_appearances} times in the sentence."

# personal attempt without string method
# using the split method to split the words in the list
# this comes at the cost of not being able to easily detect a word followed by a punctuation
# but does the job in this specific case where it is guaranteed Emma will always be isolated in the sentence

def has_substring_long(word_string):

    sentence_list = word_string.split()

    count_substring = 0

    for word in range(len(sentence_list)):
        if sentence_list[word] == "Emma":
            count_substring+=1
        
    return f"Emma has appeared {count_substring} times in the sentence."


# method proposed by Pynative using no string method
def has_substring_slicing():
    pass

def main():
    str_x = "Emma is good developer. Emma is a writer"

    print("finding Emma 2 times using the simplest method with a string method:")
    print(has_substring(str_x))
    print()
    print("finding Emma 2 times using my personal method using split:")
    print(has_substring_long(str_x))

if __name__ == "__main__":
    main()
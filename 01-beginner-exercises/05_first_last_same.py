# Exercise 5: Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.

def is_same(input_list):
    return input_list[0] == input_list[-1]


def main():

    numbers_x = [10, 20, 30, 40, 10]

    numbers_y = [75, 65, 35, 75, 30]

    print("testing isSame function on list containing the same starting and ending number:")
    print(is_same(numbers_x))

    print("testing isSame function on list containing different starting and ending number:")
    print(is_same(numbers_y))


if __name__ == "__main__":
    main()
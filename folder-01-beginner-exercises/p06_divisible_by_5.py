# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5

def is_divisible(input_list):
    print("The following numbers in the list are divisible by 5:")
    for num in range(len(input_list)):
        if (input_list[num] % 5 == 0):
            print(input_list[num])


def main():
    test_list_1 = [10, 20, 33, 46, 55]
    print("testing the list: [10, 20, 33, 46, 55]")
    is_divisible(test_list_1)

if __name__ == "__main__":
    main()
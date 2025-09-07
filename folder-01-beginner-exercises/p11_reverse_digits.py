# Exercise 11: 
# Get each digit from a number in the reverse order.

def reverse_order(num):

    num_list = list(str(num))

    len_num_list = len(num_list)

    reversed_num = ""
    
    for num in range(len_num_list -1, -1, -1):
        reversed_num += num_list[num]
    
    return reversed_num

def pynative_soln(num):
    while num > 0:
        # get the last digit
        digit = num % 10
        # remove the last digit and repeat the loop
        num = num // 10
        print(digit, end="")

def main():
    number = 7536
    print(reverse_order(number))
    pynative_soln(number)

if __name__ == "__main__":
    main()
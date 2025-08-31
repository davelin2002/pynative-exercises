# Exercise 2: Print the Sum of a Current Number and a Previous number
# Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.


# initial attempt without hint simplified the process by adding a print statement before the actual loop to account for the number starting at 0 then
# modified the inside loop to start at 1 since the 0th step was already printed outside of the loop

def current_previous_sum_1(num):
    print("Current Number 0 Previous Number 0 Sum: 0")
    for i in range(1,num):
        prev_num = i - 1
        sum = i + prev_num
        print(f"Current Number {i} Previous Number {prev_num} Sum: {sum}")

# optimizing code by updating prev with curr number (this only works if you define prev outside the for loop)

def current_previous_sum_2(num):
    prev_num = 0
    for i in range(num):
        sum = i + prev_num
        print(f"Current Number {i} Previous Number {prev_num} Sum: {sum}")
        prev_num = i

def main():
    print("my implementation:\n")
    current_previous_sum_1(10)
    print("my implementation:\n")
    current_previous_sum_2(10)

if __name__ == "__main__":
    main()
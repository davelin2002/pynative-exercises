# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a 
# new list containing odd numbers from the first list and even 
# numbers from the second list.

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

def merge_even_odd(l1, l2):
    l1_length = len(l1)
    l2_length = len(l2)
    final_list = []

    longest_list = max(l1_length, l2_length)

    for num in range(longest_list):
        if l1[num] % 2 == 1:
            final_list.append(l1[num])
        if l2[num] % 2 == 0:
            final_list.append(l2[num])
    
    return final_list
        
           

def main():
    list1 = [10, 20, 25, 30, 35]

    list2 = [40, 45, 60, 75, 90]

    # expected output: [40, 25, 60, 35, 90]

    print(merge_even_odd(list1, list2))

if __name__ == "__main__":
    main()


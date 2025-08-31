# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

# personal attempt 
# bypassing the space issue by using fstrings

def num_pattern(n):
    for i in range(1,n+1):
        number_to_print = str(i)
        print(f"{number_to_print} "*i)

# pynative solution
# a better approach is to modify the default end= command
# recall the default parameters being:
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
def num_pattern2(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i, end=" ")
        print()


def main():
    num_pattern(5)
    num_pattern2(5)

if __name__ == "__main__":
    main()
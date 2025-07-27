# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product 
# only if the product is equal to or lower than 1000. 
# Otherwise, return their sum.

def sum_or_product(num1, num2):
    
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2

def main():
    result = sum_or_product(20,30)
    print(f"This result is {result}")
    result = sum_or_product(40,30)
    print(f"This result is {result}")
        
    

if __name__ == "__main__":
    main()


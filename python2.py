import numpy as np

def add_numbers(num1, num2):
    # Create NumPy arrays from the input numbers
    arr1 = np.array(num1)
    arr2 = np.array(num2)

    return arr1 + arr2

# Example usage:
num1 = 5
num2 = 3
sum_result = add_numbers(num1, num2)
print("Sum:", sum_result)

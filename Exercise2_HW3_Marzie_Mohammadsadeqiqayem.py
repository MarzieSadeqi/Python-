# Home_Work 3
# Exercise 2
# Date: Feb 24, 2025
# Author: Marzie Mohammadsadeqiqayem

'''
Write a Python program to receive an integer (N) from the user and create a dictionary, where the 
dictionary keys are the indices (i) of the Fibonacci sequence from zero to N and the dictionary 
values are the ith values of the Sequence. For example, for N=6, the following dictionary should 
be created and shown: {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8}. Then, once the dictionary is created, 
create a plot with the x-axis being the dictionary keys and the y axis being the dictionary values. 
Make sure your plot has information such as title and axis labels. 
'''


import matplotlib.pyplot as plt

def fibonacci(n):
    """Generates a dictionary of Fibonacci sequence up to index N."""
    fib_dict = {0: 0, 1: 1}  # First two Fibonacci numbers
    for i in range(2, n + 1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]  # Calculate next Fibonacci number
    return fib_dict

def plot_fibonacci(fib_dict):
    """Plots the Fibonacci sequence."""
    x_values = list(fib_dict.keys())  # (0 to N)
    y_values = list(fib_dict.values())  # Fibonacci numbers

    plt.figure(figsize=(8, 5))  # Create a figure
    plt.plot(x_values, y_values, marker='*', color='black')  # Plot the values with black color
    plt.xlabel("Index (i)")  # Label x-axis
    plt.ylabel("Fibonacci Value")  # Label y-axis
    plt.title("Fibonacci Sequence")  # Title of the plot
    plt.grid(True)  # Add a grid
    plt.show()  # Display the plot

# Main program
N = int(input("Enter an integer N: "))  # Get user input
fib_dict = fibonacci(N)  # Generate Fibonacci dictionary
print("Generated Fibonacci Dictionary:", fib_dict)  # Print the dictionary
plot_fibonacci(fib_dict)  # Plot the Fibonacci numbers

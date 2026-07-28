# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# Function to calculate the sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function to calculate the average
def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function to find the maximum value
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# Function to find the minimum value
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# Main program
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: The number of values must be a positive integer.")
else:
    numbers = []

    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        numbers.append(number)

    print("\nResults:")
    print("Sum:    ", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))


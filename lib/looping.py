#!/usr/bin/env python3

# Function for Happy New Year countdown
def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

# Function to square integers in a list
def square_integers(numbers):
    return [x ** 2 for x in numbers]

# FizzBuzz function for numbers from 1 to 100
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

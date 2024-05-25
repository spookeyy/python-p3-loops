#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x = 10
    while x > 0:
        print(x)
        x -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    new_list = [integer ** 2 for integer in int_list]
    return new_list

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

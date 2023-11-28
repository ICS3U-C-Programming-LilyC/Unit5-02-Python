#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/27/2023
# This program will calculate the area of a triangle.
# Importing math module.
import math


# Declaring my function using parameters for the base and height of the triangle
# This function will calculate and display the area of a triangle.
def calc_area(base, height):
    # Calculations for area.
    area = (base * height) / 2

    # Displaying the area back to the user.
    print("The area is {:.2f} cm^2.".format(area))


# Using my main() function to get user input and call my calc_area function.
def main():
    # Explaining my program to the user.
    print("This program will calculate the area of a triangle.\n")

    # Getting user input.
    base_from_user = input("Enter a base for your triangle as a decimal in cm: ")
    height_from_user = input("Enter a height for your triangle as a decimal in cm: ")

    # Using a try catch to catch any erroneous inputs.
    try:
        # Converting base and height input into a decimal.
        base_as_float = float(base_from_user)
        height_as_float = float(height_from_user)

        # If statement to not allow negatives.
        if base_as_float < 0 or height_as_float < 0:
            print("Please enter a positive number.")

        # Else calling calc_area function.
        else:
            calc_area(height_as_float, base_as_float)

    # Catching any errors.
    except:
        print("Invalid input.")


if __name__ == "__main__":
    main()

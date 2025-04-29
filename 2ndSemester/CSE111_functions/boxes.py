import string
import math

def get_int(prompt):
        while True:
            num = input(prompt)
            if num.isdigit() == True:
                return int(num)
            else:
                print("Please enter a valid number")

def per_box_calc(top,bottom):
     return (top / bottom).__ceil__()

def main():
     user_items = get_int("Enter the number of items: ")
     user_per_box = get_int("Enter the number of items per box: ")

     print(f"For {user_items} items, packing {user_per_box}, you will need {per_box_calc(user_items,user_per_box)} boxes.")

main()

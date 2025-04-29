
# v = 
# π w^2 a(w a + 2,540 d) / 10,000,000,000

# v is the volume in liters,
# π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
# w is the width of the tire in millimeters,
# a is the aspect ratio of the tire, and
# d is the diameter of the wheel in inches.

import math
from datetime import datetime

def tire_shopping_list(width,diameter,a_r):
    if width == 245 and diameter == 19 and a_r == 40:
        print("Michelin Pilot Sport 4S : $450")
    elif width == 265 and diameter == 17 and a_r == 65:
        print("GoodYear Wrangler All-Terrain Adventure with Kevlar : $300")
    elif width == 205 and diameter == 16 and a_r == 55:
        print("Bridgestone Blizzak WS90 : $250")
    elif width == 215 and diameter == 18 and a_r == 60:
        print("Continental TrueContact Tour : $280")


def get_int(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Please enter a valid number")

def tire_volume_calculator(width,aspect_ratio,diameter):
    return ( (math.pi * (width**2) * aspect_ratio) * ((width * aspect_ratio) + (2540 * diameter)) ) / 10000000000

def save_to_file(width,aspect_ratio,diameter,volume):
    current_date = datetime.now()
    with open("volume.txt", mode="at") as volume_file:
        print(f"{current_date:%Y-%m-%d}, {width:.2f}, {aspect_ratio:.2f}, {diameter:.2f}, {volume:.2f}", file=volume_file)

def main():
    
    user_width = get_int("Enter the width of the tire in mm (ex 205): ")
    user_aspect_ratio = get_int("Enter the aspect ratio of the tire (ex 60): ")
    user_diameter = get_int("Enter the diameter of the wheel in inches (ex 15): ")
    end_volume = tire_volume_calculator(user_width,user_aspect_ratio,user_diameter)

    print(f"The approximate volume is {end_volume:.2f} liters")
    tire_shopping_list(user_width,user_diameter,user_aspect_ratio)
    save_to_file(user_width,user_aspect_ratio,user_diameter,end_volume)

main()
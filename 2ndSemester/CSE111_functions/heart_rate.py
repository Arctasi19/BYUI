"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your hearts maximum rate.
"""

def get_int(prompt):
        while True:
            try:
                num = int(input(prompt))
                if num in range(120):
                    return num
                else:
                     print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")

def heart_calculator(age):
    max_rate = 220 - age

    ideal_high = max_rate * 0.85
    ideal_low = max_rate * 0.65

    print(f"When you exercise to strengthen your heart, \nyou should keep your heart rate between {ideal_low:.0f} and {ideal_high:.0f} beats per minute.")
     

def main():
    user_age = get_int("Please enter your age: ")

    heart_calculator(user_age)

main()
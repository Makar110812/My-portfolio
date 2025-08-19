from time import time
from time import sleep
from math import floor

# Entering a number
num = int(input("Enter the number you want to guess: "))
# Just decorate :)
number_of_characters = len(str(num))
print('—' * (number_of_characters + len("Enter the number you want to guess: ")) + "\n")

# Entering a count of attempts
attempts = input("Enter the number of matching attempts (enter 0 or empty line for infinity): ")
number_of_characters = len(str(num))
print('—' * (number_of_characters + len("Enter the number of matching attempts (enter 0 or empty line for infinity): ")))

# Output 1000 empty lines so that the entered number cannot be seen
number_of_characters = len(str(num))
sleep(2)
print("\n" * 999)  # 999 because there will be another empty line at the end of the print
                   # (since I didn't set the "end" parameter)

start_time = time()

# Initializing the number matching functions
def selection_limited(num: int, remaining_attempts: int):
    completed_attempts = 0
    while True:
        if remaining_attempts == -1:  # It works this way
            print(f"> You lost. The number you guessed was {num}")
            return 0
        print()
        i = int(input(f"> You have {remaining_attempts} attempts to guess. Pick a number: "))
        completed_attempts += 1
        if i == num:
            end_time = time()
            result_time = floor(end_time - start_time)
            print(f"> Congratulations! You guessed it in {completed_attempts} tries and {result_time} seconds")
            return 0
        elif i > num:
            print(f"> The hidden number is less. There are {remaining_attempts} attempts left")
        elif i < num:
            print(f"> The hidden number is greater. There are {remaining_attempts} attempts left")
        remaining_attempts -= 1

def selection_unlimited(num: int):
    while True:
        completed_attempts = 0
        i = int(input(f"Pick a number: "))
        completed_attempts += 1
        if i == num:
            end_time = time()
            result_time = floor(end_time - start_time)
            print(f"Congratulations! You guessed it in {completed_attempts} tries and {result_time} seconds")
            return 0
        elif i > num:
            print(f"The hidden number is less\n")
        elif i < num:
            print(f"The hidden number is greater\n")

def selection(num: int, attempts: str):
    if attempts in ["", "0"]:
        selection_unlimited(num)
    else:
        attempts = int(attempts)
        selection_limited(num, attempts)

# Start functions
selection(num, attempts)

print("Enter numbers separated by new lines. When finished, enter an empty line.")  # Help

min_num = None  # Answer
max_num = None  #

def checking_for_fractions(num: float):  # Checking the possibility of converting to an integer
    if num == float(int(num)):
        return True
    else:
        return False

while True:
    value = input()  # Entering a value
    if value == "":  # Stopping the input
        break
    else:
        value = float(value)
    if min_num is None and max_num is None:
        min_num = max_num = value
    elif value > max_num:
        max_num = value
    elif value < min_num:
        min_num = value

if checking_for_fractions(min_num):  # Conversion to an integer, if possible
    min_num = int(min_num)           #
if checking_for_fractions(max_num):  #
    max_num = int(max_num)           #

print(f"Minimum value | {min_num}",
      f"Maximum value | {max_num}", sep="\n")

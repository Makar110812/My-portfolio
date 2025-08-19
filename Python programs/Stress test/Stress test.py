input('Для запуска нажмите ENTER. ')      # Program launch confirmation
from math import factorial                # Importing the factorial from the "math" library
from sys import set_int_max_str_digits    # Importing the limit from the "sys" library
set_int_max_str_digits(2147483647)        # Changing the limit to the maximum possible value
n = 0                                     # Setting the initial value of the "n" variable (0)
while True:                               # Creating an infinite loop
    n = n + 1                             # Adding 1 to the variable "n"
    print(factorial(n))                   # Finding the factorial of a variable "n"
    if (len(str(n))) == 2147483647:       # If the value of the "n" variable exceeds the limit,
        n = n + 1                         # then reset the "n" variable

# VARIABLES
    # Input
        # p = percent
        # i_2 = int_2
    # Output
        # i_1 = int_1
# THE MATHEMATICAL FORMULA
    # i_1 / 100 * p = i_2
    # i_1 = i_2 * 100 / p

# The code starts with line 15 (:15)



i_2 = int(input('Second int | '))
p = int(input('Percent    | '))
i_1 = i_2 * 100 / p
print('First int  |', i_1)

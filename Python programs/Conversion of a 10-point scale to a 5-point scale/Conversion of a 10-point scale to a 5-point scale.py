# Entering an estimate on a 10-point scale
evaluation_10marks = int(input('10-point scale rating | '))

# Translation of the assessment to a 5-point scale and checking the input for the correct input
if 10 >= evaluation_10marks >= 0:
    if evaluation_10marks >= 9:
        evaluation_5marks = 5
    elif evaluation_10marks >= 7:
        evaluation_5marks = 4
    elif evaluation_10marks >= 5:
        evaluation_5marks = 3
    elif evaluation_10marks >= 3:
        evaluation_5marks = 2
    elif evaluation_10marks != 0:
        evaluation_5marks = 1
    else:
        evaluation_5marks = 0
else:
    print('Error: The wrong valuation value is introduced on a 10-baral scale.')
    exit()

# Conclusion Assiting on a 5-point scale
print('5-point scale rating  |', evaluation_5marks)

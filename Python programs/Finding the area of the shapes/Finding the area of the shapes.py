# Shape selection
print('1 | Rectangle')
print('2 | Square')
print('3 | Triangle')
print('4 | Parallelogram')
print('5 | Rhomb')
print('6 | Trapezoid')
print('7 | Circle')
n = int(input())

# Finding the area of a rectangle
if n == 1:
    AB = int(input('Side AB | '))
    BC = int(input('Side BC | '))
    print('Area    |', AB * BC)

# Finding the area of a square
elif n == 2:
    a = int(input('Either side | '))
    print('Area        |', a ** 2)

# Finding the area of a triangle
elif n == 3: 
    a = int(input('Any reason                    | '))
    ha = int(input('| '))
    print('Area                          |', (a * ha) / 2)

# Finding the area of a parallelogram
elif n == 4:
    a = int(input('Any base                       | '))
    ha = int(input('The height drawn to this base  | '))
    print('Area                           |', a * ha)

# Finding the area of a rhomb
elif n == 5:
    d_1 = int(input('1st diagonal | '))
    d_2 = int(input('2nd diagonal | '))
    print('Area         |', d_1 * d_2)

# Finding the area of the trapezoid
elif n == 6:
    a = int(input('Upper base                                                        | '))
    b = int(input('Lower base                                                        | '))
    h = int(input('The height drawn from the upper base to the lower (or vice versa) | '))
    print('Area                                                              |', (a + b) * h / 2)
          
# Finding the area of the circle
elif n == 7:
    import math
    r = int(input('The radius of the circle | '))
    print('Area                     |', math.pi * r ** 2)

# Input error
else:
    print('Input error')

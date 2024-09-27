# Thayer Yang
# 27 SEP 2024
# Simple Math 2

# Task 1

price = 30.00
DISCOUNT_FACTOR = .80

new_price = price*DISCOUNT_FACTOR

print(f'A shirt that originally costs ${price:.2f} with a discount of {round((1 - DISCOUNT_FACTOR)*100)}% off now costs ${new_price:.2f}.\n')

# Task 2

length = 12
width = 8

area = length*width

print(f'A garden with a length of {length} meters and width of {width} meters have an area of {area} meters squared.\n')

# Task 3

num_of_bacteria = 10
hours = 5
GROWTH_FACTOR = 2

total_bacteria = num_of_bacteria *(GROWTH_FACTOR**hours)

print(f'Started with {num_of_bacteria} bacteria, with the bacteria multiplying by {GROWTH_FACTOR} every hour. \nAfter {hours} hours, there is a total of {total_bacteria} bacteria.\n')

# Task 4

distance = 200 #Kilometers
velocity = 90 #Kilometers per hour

time = distance / velocity #Time in hours

print(f'Owen, Koen, and Qwynn will take {time:.2f} hours to drive {distance} kilometers at {velocity} kilometers per hour.')

# Task 5

people = 23
slices = 8

slices_leftover = slices- people

if slices_leftover <=0:
    print('There are no more slices leftover.')
else:
    print(f'There are {slices_leftover} slices of pizza left over.')
'''
For Loop and Range Exercise

Use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in the variable x .  

You could cheat and just figure this out using a calculator, but...that would defeat the whole point of this course.

Can I put emoji in here? Let's see...🤗 It works!!!
'''


# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE
for i in range(10, 21):
    if i % 2 != 0:
        x += i

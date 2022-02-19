"""5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything
other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
 Enter 7, 2, bob, 10, and 4 and match the output below."""

largest_num = None
smallest_num = None
while True:
    sanswer = input('give me a number: ')
    if sanswer == 'done':
        break
    try:
        fanswer = float(sanswer)
    except:
        print('Invalid input')
        continue
    if largest_num is None:
        largest_num = fanswer
    elif largest_num < fanswer:
        largest_num = fanswer
    if smallest_num is None:
        smallest_num = fanswer
    elif smallest_num > fanswer:
        smallest_num = fanswer
print('Maximum is',int(largest_num))
print('Minimum is',int(smallest_num))

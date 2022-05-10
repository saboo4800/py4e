top = input("what number shall I go to? ")

for i in range(int(top)):
    i +=1
    if i % 3 == 0 and  i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 

#Print "FizzBuzz" if the Value Is a Multiple of Three and Five

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
else:
    print(value)
    
#Output

$./fizz-buzz-item.py
Enter an integer value: 15
FizzBuzz
$ ./fizz-buzz-item.py
Enter an integer value: 4
4


#Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five

#!/usr/bin/env python3.7

value = int(input("Enter an integer value: "))

if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)
    
#Output

$ ./fizz-buzz-item.py
Enter an integer value: 15
FizzBuzz
$ ./fizz-buzz-item.py
Enter an integer value: 4
4
$ ./fizz-buzz-item.py
Enter an integer value: 6
Fizz
$ ./fizz-buzz-item.py
Enter an integer value: 10
Buzz
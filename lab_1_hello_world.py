#Lab 1 - A Simple Function

#In python we can declare a function using the syntax def function_name():

#A function begins with def, has a name in lower case, with words separated by underscores to improve readability, a set of () which contain parameters (more on this later) and ends in :.

#Here is a very simple function that when it is called will return hello world.

# A function that prints hello world
def hello_world():
    print("hello_world")
    
    
# This line calls (runs) the function
hello_world()
    
#Save the file using file > save or command + s with the name lab_1_hello_world.py. The py on the end denotes that it is a python file.

#To run the program, enter the following command in the terminal:

python lab_1_hello_world.py

#This should return hello world.

#Returning information from a function

#When a function performs some kind of activity, by default the information it remains contained within the boundary of the function. To pass the information to other parts of your code, you need to use return. The value the function returns is called the return value and it is passed back to the line which called the function.

#Modify lab_1_hello_world.py as follows:

# A function that returns hello world
def hello_world():
    return 'hello_world'
    
# Assign the hello_world() function to a variable.
greeting = hello_world()
print(greeting)
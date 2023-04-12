#Variables
#A variable is a value that can change. They can be used to store information that can be referenced and used by programs. Instead of using the stored value directly, we can use the variable instead.

#Variables in python are declared in the format name = value. 

#Below are some examples:

a_str = "This is an example of a string in quotes" # In python the word string is abbreviated to str
my_float = 5.5
an_integer = 5 # integer is abbreviated to int
shopping_list = ["apples", "oranges", "pears"]
a_dict = {"userId": "JBloggs"} # dictionary is abbreviated to dict
my_var = another_variable # variable is abbreviated to var
test_function = my_function() #function is abbreviated to func
example_tuple = ("apple", "orange", "pear")
boolean_values = True # boolean is abbreviated to bool


#Data Types

#Strings
#In python a string, is shortened to str and refers to anything inside quotes. 
#The quotes can be double or single. The examples below are identical to python.

"The quick brown fox jumped over the lazy dog"
'The quick brown fox jumped over the lazy dog'

#If you want to include a direct quote in your sentence, then use single quotes for the string and double quotes for the direct quote.
#For example:
'The error message was "Incorrect DataType"'


#Strings, like all data types, can be assigned to a variable.
first_name = "Monty"
last_name = "Python"

#You can add strings together using variables. This concatenates them.
print(first_name+last_name)
MontyPython
#To include a space, you need to either add it to the beginning or end of your word or add it as a separate string. Fix the sentence below.
print(first_name + " " + last_name)
#Monty Python


#Using Variables in Strings

#Imagine we want to use the value of a variable in the middle of a string. This can be done a few ways in python.

.format()

#In this method you can use the {} in your string to indicate where the variable should go. Then use .format(variable_name) after the quotation marks. 
If you have multiple variables, for each variable you use a {}. In the .format() separate each variable with a comma. For example .format(variable_1, variable_2).

#Try this in the interactive python. Type or paste each line after the >>>.
first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}".format(first_name, surname))


f strings

#Since python version 3.6 it has been possible to use a format called f-strings to include variables in your strings. Some people find this format easier to read.

firstname = "Jane"
surname = "Doe"

print(f"My first name is {firstname}. My family name is {surname}")


New Lines and indentation

#If you want your text to go over several lines you can use \n and \t. The \ character is called an escape character.
#The n tells python to put the text on the next line.
#The t tells python to add a tab spacing.

string = "This is a string over\nthree lines\n\twith the third line indented"
print(string)

This is a string over
three lines
        with the third line indented


#Numbers
Integers
An integer is a whole number such as 50. The data type integer is abbreviated to int.

#Floating point numbers
A floating point number is a number followed by a decimal point such as 50.5.


#Using Number Variables in Strings
In the previous section on strings you learnt that you can use the + to add strings together to form sentences. You also learned that you can insert variables into a sentence using the {}.

What happens if we try to use a number with these two different methods?

#Try the following code.
my_int = 50
sentence = "The total comes to: "

print(sentence + my_int)

#Fix the error by converting the int data type to a str data type.
my_int = 50
sentence = "The total comes to: "

print(sentence + str(my_int))


#Dictionaries
A dictionary is a way of storing related information in key-value pairs. It uses a key as an identifier and a value to store the information. For example, the key could be first_name and the value could be Ada.

A dictionary when written in python would look like {"first_name":"Ada"}. A dictionary in python is abbreviated to dict and has the following syntax {"key":"value"}. The key is a string providing an identifier and the value can be the same kind of values you would store in a variable.

#Creating, Reading, Updating and Deleting values in a dictionary
#Create


#Dictionaries can be created by assigning the key-values you want to store in the dictionary.

#Using the python interactive mode, try the following:
user = {"first_name":"Ada"}
print(user)
{'first_name': 'Ada'}


#Read
#To read the value associated with a key, you need to provide the name of the dictionary and the the value of the key inside square brackets.

#Try the following:

user = {"first_name":"Ada"}
print(user["first_name"])
Ada

#Update
#Add a key-value
#Dictionaries are mutable, which means they can be changed after you create them. You can add, update or delete the key-value pairs in a dictionary.

#To add an additional key-value to a dictionary, provide the dictionary name, the new key in [] and a value after an = sign.

#Try the following:
user["family_name"] = "Byron"
print(user)
{'first_name': 'Ada', 'family_name': 'Byron'}


#Modify a value
#To modify a value in a similar way to adding it. You provide the new value after the = sign.

# the following:
user["family_name"] = "Lovelace"
print(user)
{'first_name': 'Ada', 'family_name': 'Lovelace'}

#Delete a Key-Value Pair
#To remove a key-value pair you use the del statement with the name of the dictionary and the key you want to delete.

 user["family_name"]
 print(user)
{'first_name': 'Ada'}


#Summary
#A dictionary, like a variable can contain other data types, including other dictionaries and lists. {}`. You will use dictionaries a lot in AWS as input and outputs.




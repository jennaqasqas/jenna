#File: homework1. py
# --- Variables and Data Types ---

a = 10
print(a)
print(type(a))

b = 1.5
print(b)
print(type(b))

c = 3j
print(c)
print(type(c))

d = "hello"
print(d)
print(type(d))

e = [1, 2, 3]
print(e)
print(type(e))

f = {"name": "Ellen", "fav fruit": "strawberry"}
print(f)
print(type(f))

g = (1, 2)
print(g)
print(type(g))

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))

i = True
print(i)
print(type(i))

j = None
print(j)
print(type(j))

k = [True, "blue", 12]
print(k)
print(type(k))

l = str(14)
print(l)
print(type(l))

m = 1e4
print(m)
print(type(m))

#1. 9
#2. int, float, complex, string, list, dictionary, tuple, boolean, nonetype
#3. b & m, d & l, e & h & k
#4. string; str() converts an integer into a string
#5. set. 
n = {"brush", "paste", "basket"}
print(n)
print(type(n))

# -- Booleans --
print(10 > 9) # True, 10 is greater than 9
print(10 == 9) # False, 10 is greater than 9
print(10 <= 9) # False, 10 is greater than 9
print(bool("abc")) # True, string
print(bool(123)) # True, non zero integer
print(bool(0)) # True, 10 is greater than 9
print(bool(["apple", "cherry", "banana"])) # True, set 
print(bool(True)) # True,boolean true
print(bool(False)) # False ,boolean false
print(bool(0)) # False, zero integer
print(bool("")) # False, empty or null
print(bool(" ")) # True, space string
print(bool(())) # False, null entry
print(bool([])) #false, null list
print(bool({})) # False,  null empty set
print(bool(True and False)) # False,  False overpowers
print(bool(True and True)) # True,  only true
print(bool(False and False)) # false,  only false
print(bool(True or False)) # True,  defaults true
print(bool(False or False)) # False,  only false is an option
print(bool(True or True)) # True,  only true options
print(bool(not(False))) # True, isn't false
print( bool(not(True))) # False,  isnt true

#null or empty sets return false, non zero integers return true
#true or false = true
#print(bool(1e4)). True because this is a float
#print(6 > 8)). False; 6 is less than 8

# --- Operators ---
# --- Arithmetic Operators ---
print(10 + 5) # 15, addition
print(10 - 5) # 5, subtraction
print(2 * 4) # 8, multiply
print(6 / 3) # 2, division
print( 5 % 2) # 2.0, integer division of 5 by 2
print( 3 ** 2) #9, 3 to the power of 2
print(15 // 2) #7, integer division
# --- Comparison Operators ---
print(5 == 2) # false; not equal
print(10 != 10) # false, ! means not equal to but theyre equivalent
print(2<5) # true, 2 less than 5
print(12>5) #true, 12 greater than 5
print(5 <= 6) #true, 5 is less than 6
print(1 >= 10) #false, 1 is less than 10
# --- Assignments Operators ---
x = 5
x += 5
print(x) #10, added 5
x -= 4
print(x) #6, 10-4
x *= 3
print(x) #18, 9 times 3

# -- Logical Operators --
#1. and only returns true if both conditions are true, otherwise it's false.
print(5 > 2 and 10 > 3) #true, both statements are true
print(5 > 2 and 10 < 3) #false, one statements is false
#2. logical operator that returns true if at least one condition is true and only returns false if both are false
print(5 > 2 or 10 < 3) #true, one statements is true
print(5 < 2 and 10 < 3) #false, both statements are false
#3. reverses the boolean value
print(not 5 > 3) # false, 5 is greater than 3
print(not 5 < 3) # true, 5 is greater than 3

# --- More questions ---
#1. / is regular division, while // is integer division and rounds down
#2. // is integer division rounded down, % is the remainder
#3. %
print(13 % 3) #1, remainder when 13 is divided by 3
#4. assignment operators update a variable's value by an operation

#--- Strings ---
my_string = "hello"
print(my_string) # prints hello
print(my_string[0]) # prints h
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints 1
print(my_string[4]) # prints o
print(my_string[-1]) # prints o
print(my_string[1:3]) # prints el
print(my_string[0:5:2]) # prints hlo
print(len(my_string)) # prints 5
print(my_string + "goodbye") # prints hellogoodbye
print(7 * my_string) # prints hellohellohellohellohellohello...

#1. slicing is taking only part of the string by indexing it, whenever i used the square bracktes []
#2. 
name = "Oski"
print("Hello, my name is", name) #print Hello, my name is Oski
#3.
name = "Oski"
print(f"Hello, my name is {name}") #prints Hello, my name is Oski
#4. the first one used a comma to combine the text and variable, but the second used a f-string and embedded the variable inside the string

# --- Terminal Commands ---
# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Lists files and folders in the current directory
# Example: ls

# ls -a
# Lists all files, including hidden files (starting with .)
# Example: ls -a

# mkdir
# Creates a new directory
# Example: mkdir projects

# cat
# Displays the contents of a file in the terminal
# Example: cat jenna.txt

# pwd
# Prints the full path of the current directory
# Example: pwd

# cd ..
# Moves up one directory to the parent folder
# Example: cd ..

# cd .
# Returns the current directory
# Example: cd .

# cd ~
# Takes you to the home directory
# Example: cd ~

# cp
# Copies files or folders from one location to another
# Example: cp hw1.txt backup.txt

# mv
# Moves or renames files and folders
# Example: mv hw1.txt newname.txt

# rm
# Deletes files or folders permanently (use with caution)
# Example: rm file.txt

# clear
# Clears text from the terminal screen
# Example: clear

# grep
# Searches for text patterns inside files
# Example: grep "hello" notes.txt

#1. touch
# Creates a new empty file or updates the timestamp of an existing file
# Example: touch notes.txt

# echo
# Prints text to the terminal or writes text into a file
# Example: echo "Hello world" > hello.txt

# man
# Displays the manual (help page) for a command
# Example: man ls

#2. ls only shows visible files and folders, while ls -a shows all files, even hidden ones
#3. a hidden file has a name that starts with a "." 
#4. ls -l
# Shows files in a detailed list with permissions, size, and date
# ex: ls -l

# rm -r
# Deletes a folder and everything inside it
# ex: rm -r flop_folder

# cp -r
# Copies a folder and all its contents
# ex: cp -r project project_copy



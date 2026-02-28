# 1. Git is a version control system used to track changes in code locally. GitHub is a cloud-based platform that hosts Git repositories and allows collaboration.

# 2. The terminal is the application that lets you interact with your computer using text commands. The Command Line is the interface inside the Terminal where you type commands.

# 3. A local repository is stored on your computer, but a remote repository is stored online and can be shared.

# 4. Version Control tracks changes to files over time so you can restor past versions.

# 5. The staging area is a place where changes are prepared before being committed to the repository.

# 6. git add adds changes from your working directory to the staging area.

# 7. git commit saves the staged changes to the local repository with a message describing the changes.

# 8. git push sends your committed changes from your local repository to a remote repository.

# 9. git status shows the current state of your repository, including staged, unstaged, and untracked files.

# 10. git pull downloads changes from a remote repository and updates your local repository.

# 11. pwd prints your current directory path.

# 12. ls lists files and folders in the current directory.

# 13. cd changes the current directory.

# 14. nano opens the text editor in the terminal to create or edit files.

# 15. touch creates a new empty file.

# 16. mv moves or renames a file or directory.

# 17. rm deletes a file (or directory if used with options like -r).

# 18. cat displays the contents of a file in the terminal.

## 3.2 - a directory tree
#1. pwd
#2. ls
#3. cd ../brianna_repo. git pull origin main
#4. mv ../brianna_repo/homework.py homework/
#git add homework/homework.py
#git commit -m "Updated homework.py"
#git push
# cd ../judy_decal
# ls
# git add .
# git commit -m "commit message"
# git push origin main
# DEBUGGINH
# git pull origin main
# git push origin main
# ~/Recent


## 4 Homework Review
## 4.1 Data Types
def checkDataType(value):
    return type(value).__name__

## 4.2 Conditionals
def evenorodd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
## 5 Loops
def sum_loop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

## 6.1 Lists
def duplicate_list(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

## 6.2 Debugging
# there's no colon after the first line!
def square(num):
    return num * num

print(evenorodd(11))
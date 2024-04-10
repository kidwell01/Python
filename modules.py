import re

# Your code goes here
find_members = []
word_to_find = "find"

dir(re)
#help(re)
#Use dir to get a list of the attributes and iterate over them
functions = dir(re)
for function in functions:
    if word_to_find in function:
        find_members.append(function)
        
#sorting the list aphabetically
find_members.sort() 

#print the sorted list
print(find_members)  

'''
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)

print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
print('=========')

for x in mylist:
    print(x)
'''
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

#adding elements into the numbers list
numbers.append(1)
numbers.append(2)
numbers.append(3)

#adding elements into the strings list
strings.append("hello")
strings.append("world")




# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
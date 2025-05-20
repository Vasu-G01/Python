"""
A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0 to 9, or the names of
all the people in your family.
"""

#square brackets ([]) indicate a list

students=["vasu","rahul","fahad","siam"]
print(students)

'''When we ask for a single item from a list, Python returns just that ele-
ment without square brackets'''

print(students[0].title())
print(f"{students[2].title()} is a great student")

'''Most lists you create will be dynamic, meaning you’ll build a list and then
add and remove elements from it as your program'''

#Modifing List
students[0]="shivam";
print(students)
#Output : ['shivam', 'rahul', 'fahad', 'siam']

#You might want to add a new element to a list for many reasons.

students.append("vasu")  # Note : you can not add element at specific Position
print(students)

'''You can add a new element at any position in your list by using the insert()
method. You do this by specifying the index of the new element'''

students.insert(2,"harry")
print(students)


#Often, you’ll want to remove an item or a set of items from a list.
del students[2]
print(students)


popped_students=students.pop()
print("Popped students : ",popped_students)
print("students : ",students)



'''Sometimes you won’t know the position of the value you want to remove
from a list.'''

age=[19,18,18,43,22]
age.remove(18)
age.remove(18)
'''The remove() method deletes only the first occurrence of the value you specify. If there’s
a possibility the value appears more than once in the list, you’ll need to use a loop'''
print(age)

'''the order of the list to store them alphabetically,The sort() method changes the order of the list permanently'''
students.sort()
age.sort()
print(students)
print(age)

students.sort(reverse=True) #You can also sort this list in reverse-alphabetical order 
print(students)

print("Lenght of Student List : ",len(students))  
'''You can quickly find the length of a list by using the len() function.'''

#!/usr/bin/env python
# coding: utf-8

# In[3]:


""" python variables and constants"""

count = 100
emp_name = "robin"
a1,a2,a3 = 44,"apple",6.2

print(count)
print(emp_name)
print(a1)
print(a2)
print(a3,emp_name)

b = c = a = 6
print(a,b,c)


PI = 3.14
GRAVITY = 9.8
print(PI,GRAVITY)



# In[4]:


"""python classes and objects"""

class Myfirstclass:
    #constructor method
    def __init__(self,a,b):
        print("constructor is working")
        self.aa = a
        self.bb = b
    def display(self):
        print("values from constructor {0} , {1}".format(self.aa,self.bb))
    


# In[8]:


"""python classes and objects"""

#creating a new object for the class 
obj1 = Myfirstclass(20,30)

#calling display function
obj1.display()


# In[6]:


"""python classes and objects"""

#creating a new object for the class 
obj2 = Myfirstclass(10,20)

#creating a new attritube "c"
obj2.c = 50

print(obj2.aa,obj2.bb,obj2.c)


# In[9]:


"""python classes and objects"""

#deleting object attributes and object

print(obj1)

del obj1.aa

print(obj1)

del obj1


# In[10]:


print(obj1)


# In[18]:


"""python array Implementation"""

arr = [1,2,3,4,5]
print(arr)

arr1 = ["a","ab", "cc"]
print(arr1)

#finding the length of an array

length = len(arr1)
print(length)

print(len(arr))

#adding element to array using append

arr.append(7)
print(arr)

#removing elemts from array

del arr[2]
print(arr)

arr.remove(7)
print(arr)

arr.pop(3)
print(arr)

#modifying elements of an array using indexing

arr[1] = 10
arr[-1] = 20
print(arr)

# concatination of two arrays using + operator

arr = arr + [5,7,8]
print(arr)


# In[21]:


"""python array Implementation"""

#Repeating elements in an array

a = ['b']
a = a * 3
print(a)

#slicing an array

print(arr[1:4])
print(arr[:3])
print(arr[-4:])
print(arr[-3:-1])

# Declaring and defining multidimensional array

multd = [[1,2],[5,4],[4,5],[8,9]]
print(multd)
print(multd[0])
print(multd[3])
print(multd[2][1])


# In[ ]:





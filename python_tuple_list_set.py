#!/usr/bin/env python
# coding: utf-8

# In[35]:


"""operations on tuple"""

#creating an empty tuple
tuple1 = ()
print(tuple1)

#initiliazing the tuple
tuple2 = (1,2,3)
print(tuple2)

tuple3 = (1,"helo",0.9)
print(tuple3)

type(tuple3)

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');


tup3 = tup1 + tup2;
print (tup3);

tup = ('physics', 'chemistry', 1997, 2000);
print (tup);
del tup;



# In[4]:


price = {1,2,9,5,5,5,8,8}
print(price)


# In[6]:


pric = {1,2,9,5,5,5,8,8}
print(pric)


# In[28]:


dir(tuple)


# In[18]:


"""operations on lists"""

courses = ["CNS", "EP" ,"PFSD","CC","MP2","DS"]
print(courses)


#finding the length of an list

length = len(courses)
print(length)


#removing elemts from list

del courses[2]
print(courses)

courses.remove("CNS")
print(courses)

courses.pop(3)
print(courses)

#modifying elements of an list using indexing

courses[1] = "JAVA"
courses[-1] = "Python"
print(courses)

# concatination of two lists using + operator

courses = courses + ["C","MSWD"]
print(courses)

#sort the list
courses.sort()
print(courses)

#reverse a list

courses.reverse()
print(courses)


# In[30]:


"""operations on set"""

#creating a set
courses = {"CNS", "EP" ,"PFSD","CC","MP2","DS"}
print(courses)

#add a element in set
courses.add("MSWD")
print(courses)

#clear a set 
courses.clear()
print(courses)

courses = {"CNS", "EP" ,"PFSD","CC","MP2","DS"}
courses1 = {"CNS", "MSWD" , "CC" , "MP1",}

# differnce (A-B) and (B-A)
print(courses.difference(courses1))


# In[31]:




phonebook = {'name':'Likhila', 'number':'123','email':'123@gmail.com'}


# In[16]:


"""operations of str"""


name = "LikHila"
nickname = "Likki"
sen = "I am student"
print(name.capitalize())

print(name.casefold())

print(name.count(nickname))

print(name.center(15,'a'))

print(sen.endswith('student'))

print(sen.find('am'))

print(sen.index('am'))


# In[27]:


"""operations on dict"""

phonebook = {'name':'Likhila', 'number':'123','email':'123@gmail.com'}

phonebook.clear()
print(phonebook)

phonebook = {'name':'Likhila', 'number':'123','email':'123@gmail.com'}
y = phonebook.copy()
print(y)

y = phonebook.get("name")
print(y)

y = phonebook.items()
print(y)

print(phonebook.keys())

phonebook.update({"number": "190032110"})
print(phonebook)


# In[ ]:





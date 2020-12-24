#!/usr/bin/env python
# coding: utf-8

# In[25]:


"""Python keywords and identifiers"""

#True False

print(5==5)
print(5>5)

#None
print(None == None)

def a_None():
    a = 1
    b = 2
    c = a + b
   
x = a_None()
print(x)

#and or not

print(True and False)
print(True or False)
print(not True)

#as

import math as mymath
print(mymath.cos(mymath.pi))

#break and continue

for i in range(0,8):
 if(i==5):
    break
 else:
    print(i)
    continue
print(i)



# In[27]:


#class and def

class Exampleclass:
    def function1(parameters):
        print("I am function1")
    def function2(parameters):
        print("I am function2")
obj = Exampleclass()
obj.function1()
obj.function2()


# In[28]:


#del
#if
#elif
#else
#for
#return
#while


# In[50]:


#try...raise...except...finally

try:
    x= 9
    raise BufferError
except ArithmeticError:
    print("this is ZeroDivisionError")
except:
    print("Division is not possible")

finally:
    print("ended")


# In[32]:


#from...import
import math
from math import cos
print(cos(math.pi))


# In[42]:


#global
gobalvar = 15 
def read1():
    print(gobalvar)
def write1():
    global gobalvar 
    gobalvar = 5
    print(gobalvar)
def readwrite():
    gobalvar = 10
    
    
read1()
write1()
readwrite()
print(gobalvar)


# In[52]:


#lambda
a = lambda x:x*2
for i in range(1,6):
    print(a(i))
    


# In[ ]:


#nonlocal
#with
#yield



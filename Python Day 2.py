#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Task 1

a = [1,'a',2,'b',3,4,55,'asit','nimesh']
str_list = []
int_list = []

for index in a:
    
    if type(index)==str:
        str_list.append(index)
    
    else:
        int_list.append(index)


print("Maximum in int list: ", max(int_list))
print("Minimum in int list: ", min(int_list))

str_list.reverse()
print("Reversed List in str list", str_list)
    
    


# In[9]:


# Task 2

student = {}

no_input = input("Enter Number of Students : ")
no = int(no_input)

for index in range(no):
    
    
    dict_name = {}
    
    rollno = input("RollNo :" )
    name = input("Name :" )
    marks = input("Marks :" )
    
    mark = int(marks)
    
    if mark>90 and mark<100:
        grade = 'A'
    elif mark>80 and mark<90:
        grade = 'B'
    elif mark>60 and mark<80:
        grade = 'C'
    elif mark>40 and mark<60:
        grade='D'
    elif mark==40 and mark<40:
        grade='Fail'
    else:
        grade='Invalid Marks'
    
    dict_name.update(([('rollno',rollno)]))
    dict_name.update(([('name',name)]))
    dict_name.update(([('marks',marks)]))
    dict_name.update(([('grade',grade)]))
    
    
    student.update(([('s'+str(index),dict_name)]))
    
print(student)


# In[ ]:





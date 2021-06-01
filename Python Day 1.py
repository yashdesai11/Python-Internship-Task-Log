#!/usr/bin/env python
# coding: utf-8

# In[69]:


#Task1

ls = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6, ['d', 'e', 'f'], 7, 'g', 8, 'h',
 [9, 10, 'i', 'j'],11,'aansh',["Priya"],[99,"softvan","nimesh",99],"hello"]

for index in ls:
    if type(index)== list or type(index)==str:
        if type(index)==list:
            for val in index:
                if type(val) == str:
                    print(' ',val)
                else:
                    print(val)
        if type(index)==str:
            print(' ',index)
        
    else:
        print(index)
        


# In[91]:


#Task 2

student={}

no_input = input("Enter Number of Students :" )

no = int(no_input)

for n in range(no):
    
    rollno = input("RollNo :" )
    name = input("Name :" )
    marks = input("Marks :" )
    
    
    student.update([('roll_no'+str(n),rollno)])
    student.update([('name'+str(n),name)])
    student.update([('marks'+str(n),marks)])
    
print(student)
    


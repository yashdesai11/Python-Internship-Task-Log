#!/usr/bin/env python
# coding: utf-8

# In[ ]:


studentInfo = open("studentInfo.txt", "w+")
studentMarks = open("studentMarks.txt", "w+")

aGrade = open("Agrade.txt", "w+")
bGrade = open("Bgrade.txt", "w+")
cGrade = open("Cgrade.txt", "w+")

inp = int(input("Enter Number of Students : "))

def markie(markss,rooo,naa):
    if markss>80 and markss<100:
        aGrade.write(str(markss))
        aGrade.write(str(rooo))
        aGrade.write(naa)
    elif markss>60 and markss<80:
        bGrade.write(str(markss))
        bGrade.write(str(rooo))
        bGrade.write(naa)
    else:
        cGrade.write(str(markss))
        cGrade.write(str(rooo))
        cGrade.write(naa)

for val in range(inp):
    roll_no = int(input("Enter Roll Number: "))
    studentInfo.write(str(roll_no))
    studentMarks.write(str(roll_no))
    name = input("Enter Name: ")
    studentInfo.write(name)
    
    temp = 3
    for fet in range(temp):
        marks = int(input("Enter Marks {} : ".format(fet)))
        studentMarks.write(str(marks))
        studentMarks.write("\n")
        markie(marks,roll_no,name)
        
    studentMarks.write("\n")


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task1

fn = input("Enter filename you want to edit : ")

if (fn == "demo.txt"):
    no = int(input("Enter number of lines to write: "))
    f = open("demo.txt","w+")
    
    words = 0
    char_withspace = 0 
    char_withoutspace = 0
    
    
    for line in range(no):
        lines = input("Enter Line ---: ")
        f.write(lines)
        f.write("\n")
        l = lines.strip("\n")
        wordss = l.split()
        words += len(wordss)
        char_withspace+= len(l)
        char_withoutspace += len(lines)
        
    f.close()
    print("No. of Lines: ",no)
    print(" :",words)
    print(" :",char_withspace)
    print(" :",char_withoutspace)
    
else:
    print("Filename doesn't exit")


# In[ ]:


#Task 2 

no = int(input("Enter number of lines to write: "))
f = open("demo.txt","w+")

for line in range(no):
    lines = input("Enter Line ---: ")
    f.write(lines)
    f.write("\n")

f.close()

#Reverse the list 
fn = open("demo.txt","r+")
linee = fn.readlines()
fnn = open("dummy.txt","w+")
for line in reversed(linee):
    fnn.write(line)
fnn.close()

#Replace the word
x=input("Enter word to replace : ")
y=input("Enter word for replacement: ")

with open('dummy.txt', 'r+') as file :
    filedata=file.read()
    
filedata = filedata.replace(x, y)

with open('dummy.txt', 'r+') as file:
    file.write(filedata)


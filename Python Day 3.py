#!/usr/bin/env python
# coding: utf-8

# In[123]:


import numpy as np 

no_list = int(input("Enter Number of List you want : "))


#list is mutable hence for storing list dictionary is used
dic = {}


for nolis in range(no_list) :
    name=[]
    
    no_element = int(input("Enter Number of Element you want in list {}: ".format(nolis)))
    
    for noel in range(no_element) :
        element = int(input("Enter element {}: ".format(noel)))
        name.append(element)
            
    dic.update([('ls'+str(nolis),name)])
    
print(dic)


# Functions

def concaten(value):
    final = []
    for ind in range(value):
        final = final + dic.get('ls'+str(ind))
    return final
       
        
def sqaure(listie):
    sumee = []
    for li_val in listie:
        sumee = sumee + list(map(lambda x: x*x,listie))
        return (sumee)

    
def odd(listiee):
    odde = []
    for li_val in listiee:
        odde = odde +list(filter(lambda x: (x % 2 != 0), listiee))
        return (odde)

#-----    
    
no_li = input("Input Which Operation To Perform : ")

if(no_li=='1'):
        print("First List: ",dic.get('ls0'))
    
    
elif(no_li=='2'):
        a = dic.get('ls0')
        b = dic.get('ls1')
        c = a + b
        print("Max and Min Values : ")
        print(max(c),min(c))
    
elif(no_li=='3'):
        fi = dic.get('ls0')
        se = dic.get('ls1')
        ti = dic.get('ls2')
        arr = [fi,se,ti]
        sumie=np.sum(arr,0)
        print("Sum of All Elements in List: ",sumie)
    
elif(int(no_li) > 3 ):
        int_l = int(no_li)
        final_list = concaten(int_l)
        print("Final List: ",final_list)
        print("Sqaure : ",sqaure(final_list))
        print("Odd : ",odd(final_list))
        


# In[ ]:





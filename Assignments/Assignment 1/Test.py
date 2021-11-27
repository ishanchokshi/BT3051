#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Allowed libraries: numpy
import numpy as np

def pascals_triangle(n):
    """
    Write your code here.
    Remember to return the values.
    """
    triangle = np.zeros((n,n))
    for i in range(n):
        triangle[i][0] = 1
        triangle[i][i] = 1
        if i>1:
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
    
    for i in range(n):
        for j in range(i+1):
            print(int(triangle[i][j]), end = ' ')
        print("\n")    
    
    
        

if __name__ == "_main_":
    fin = open("q3_test.txt")
    n = int(fin.read().splitlines()[0])
    fin.close()

    n = int(input("Enter a number : "))

    # Add your code here
    pascals_triangle(n)


# In[ ]:





# In[ ]:





# In[ ]:





# %%

import numpy as np
def pascals_triangle(n):
    """
    Write your code here.
    Remember to return the values.
    """
    # For n>1, the formula for each element in line 'n' in Pascal's triangle is (n-1)Cr where 0 <= r <= n-1
    print(1) #Printing the first row
    for i in range(1,n):
        for j in range(0,i+1): # So the inner loop runs till j = i
            print(np.math.factorial(i)//(np.math.factorial(j)*np.math.factorial(i-j)), " ", end = "") # Calculates the value of iCj
        print() # Go to the next line

if __name__ == "__main__":
    fin = open("q3_test.txt")
    n = int(fin.read().splitlines()[0])
    fin.close()

    # Add your code here
a = pascals_triangle(n)

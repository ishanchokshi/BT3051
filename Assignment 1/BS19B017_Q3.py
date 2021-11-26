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
    
    
        

if __name__ == "__main__":
    fin = open("q3_test.txt")
    n = int(fin.read().splitlines()[0])
    fin.close()


# Add your code here
a=pascals_triangle(n)
print(a)

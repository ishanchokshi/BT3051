import matplotlib.pyplot as plt
from numpy import random
# no other libraries are allowed

def func(x):
    return 1/x

def Estimated_area_under_curve(func, lower_limit, higher_limit):
    """
    Estimate the area under the curve for a given function using the method discussed in the class using random numbers.
    Assume the input function to be monotonic.
    """
    area = 0
    """ Add your code here """
    points = []
    for i in range(100000): #Generate random points within the rectangle
        x = random.uniform(0.5,2)
        y = random.uniform(0,max(func(0.5),func(2)))
        points.append((x,y))
    interior = 0
    for i in range(len(points)):
        if(points[i][1]-func(points[i][0])<=0):
            interior = interior + 1 #Count the number of points generated which are under the curve
    area = (interior/100000)*(2-0.5)*(max(func(0.5),func(2))) # Area = (Fraction of points generated within the rectangle which are under the curve) * Area of the rectangle formed
    return area

Estimated_area = Estimated_area_under_curve(func, 1/2, 2)
estimated_e = 0
# Find the area under the curve analytically. Equating the analytical expression and with the estimated value, find the value of the irrational number e. Hint, use log to the base 2.
""" Add your code here """
estimated_e = 2**(2/Estimated_area) #2ln2 = area => 1/log_2(e) = area/2 => e = 2^(2/area)

print("e = ", str(estimated_e))
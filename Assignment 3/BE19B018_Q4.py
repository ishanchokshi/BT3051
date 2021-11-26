def k_closest_points(x_array, y_array, point, k):
    """
    (list of float, list of float, tuple of two floats, int) -> (list of float), (list of float)
    
    >>> k_closest_points([1.0, 1.0, 3.0, 5.0], [0.0, 3.0, 4.0, 5.0], (0.0, 0.0), 2)
        [1.0, 1.0], [0.0, 3.0]
    """
    """ Add your code here """
    #We can use the inbuilt sorted() function of python which has a Time complexity of O(nlogn)
    coordinates = [[i,j] for i,j in zip(x_array,y_array)]
    x_closest = [(sorted(coordinates, key=lambda p: (p[0]-point[0])**2 + (p[1]-point[1])**2)[:k])[i][0] for i in range(k)] #Store x-coordinates
    y_closest = [(sorted(coordinates, key=lambda p: (p[0]-point[0])**2 + (p[1]-point[1])**2)[:k])[i][1] for i in range(k)] #Store y-coordinates
    #Total complexity of program = nlogn + n which belongs to O(nlogn)
    return x_closest,y_closest
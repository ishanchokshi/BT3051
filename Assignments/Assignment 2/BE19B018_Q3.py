# DSA for Biology - Assignment 2 
# Template for question  - Conway's Game of Life

class Simulate_Conways_Game_of_Life():
    def __init__(self, MyMatrix):
        self.matrix = MyMatrix
        """ Add your code here """

    """ Add your functions here """
    
    def neighbour_check(self, current_row , current_column): # Will check and store the values of all the valid neighbours of a cell
        neighbour_list = [] #Append the values of all the valid neighbours of the current cell
        for row in range(-1,2):
            for column in range(-1,2):
                neighbouring_row = current_row + row
                neighbouring_column = current_column + column 
                valid_neighbour = True #This acts like a flag to check if the neighbour of the current cell is exists or not
                if((neighbouring_row)==current_row and (neighbouring_column)==current_column):
                    valid_neighbour = False
                if((neighbouring_row)<0 or (neighbouring_row)>=len(self.matrix)): #This checks for corner and edge cases
                    valid_neighbour = False
                if((neighbouring_column)<0 or (neighbouring_column)>=len(self.matrix[0])): #This also checks for corner and edge cases                    
                    valid_neighbour = False
                if(valid_neighbour==True):
                    neighbour_list.append(self.matrix[neighbouring_row][neighbouring_column])
        return neighbour_list   


    def simulate_one_step(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        indices = [] # Will store the indices of the cells whose status needs to be changed 
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[row])):
                find_neighbours = self.neighbour_check(row , column) #Find the number and status of the valid neighbours of each cell
                live_neighbours = sum(find_neighbours) # Will caclulate the number of  valid live neighbours for each cell
                
                if(self.matrix[row][column]==1): 
                    if(live_neighbours < 2 or live_neighbours > 3):
                        indices.append((row,column))   #Finding the positions of the elements whose current status needs to be changed     
                   
                if(self.matrix[row][column]==0):
                    if live_neighbours == 3:
                        indices.append((row,column))
                    
        for (i,j) in indices:
            self.matrix[i][j] = self.swap(self.matrix[i][j]) #Changing th status of the selected cells
            
            
    def swap(self,element): #The swap function to change the status
        if(element==1):
            element = 0
        else:
            element = 1
        return element

                
    def final_output(self):
        """
        Return the output of the 39th step 
        """
        for i in range(39):
            self.simulate_one_step()
        return self.matrix 


Glider = [[0 for i in range(100)] for j in range(100)]
Glider[1][2] = 1
Glider[2][3] = 1
Glider[3][1:4] = [1,1,1]

# 0 - Dead cell, 1 - Live cell
Game1 = Simulate_Conways_Game_of_Life(Glider)
Step_39 = Game1.final_output()
from matplotlib.pyplot import matshow

matshow(Step_39)
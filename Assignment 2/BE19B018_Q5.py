# DSA for Biology - Assignment 2
# Template for question  - Stacks and queues

""" Add your classes/functions here """
#First create a class for Stack
class Stack:
    def __init__(self,capacity):
        self.arr = [None]*capacity
        self.max_capacity = capacity
        self.size = 0
        self.top = -1
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.max_capacity
    
    def push(self,element):
        if (self.isFull()):
            print("Stack is full")
        else:
            self.top = self.top + 1
            self.size = self.size + 1
            self.arr[self.top] = element
            
    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
        else:
            a = self.arr[self.top]
            self.top = self.top-1
            self.size = self.size-1
            return a
        
    def peek(self):
        if(self.isEmpty()):
            print("Stack is Empty")
        else:
            return self.arr[self.top]
#Create a class for Queue
class Queue:
    def __init__(self,capacity):
        self.queue = [None]*capacity
        self.max_size = capacity
        self.size = 0
        self.front = 0
        
    def size_queue(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def isFull(self):
        return self.size == self.max_size
    
    def enqueue(self,element):
        if(self.isFull()):
            print("Queue is full")
        else:
            pos = (self.front+self.size)%self.max_size
            self.queue[pos] = element
            self.size = self.size+1
            
    def dequeue(self):
        if (self.isEmpty()):
            print("Queue is Empty")
        else:
            a = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front+1)%(self.max_size)
            self.size = self.size-1
            return a
        
    def front(self):
        if(self.isEmpty()):
            print("Queue is Empty")
        else:
            return self.queue[self.front]


def Simulate_Sandwitch_for_Students(Students, Sandwitch):    
    """ 
    (list of integers, list of integers) -> (int)
    Returns the number of students that were unable to eat.
    >>> Simulate_Sandwitch_for_Students([1,1,0,0], [0,1,0,1])
    0
    >>> Simulate_Sandtch_for_Students([1,1,1,0,0,1], [1,0,0,0,1,1])
    3
    """
    """ Add your code here """
    stack = Stack(len(Sandwitch)) #Create a stack object for the list of sandwitches
    queue = Queue(len(Students))  #Create a queue object for the list of students
    for i in range(0,len(Students)):
        queue.enqueue(Students[i]) #Push all the elements in the Sandwitch list into the stack
    l_sandwich = len(Sandwitch)
    for i in range(l_sandwich):
        stack.push(Sandwitch[l_sandwich-i-1]) #Enqueue the elements in the Students list into the queue
    students_without_lunch=0
    while(students_without_lunch < queue.size_queue()): #As long as the number of students in the queue are more than the number of students without lunch
        student_at_front= queue.dequeue() #Remove the student at the front of the queue
        if(student_at_front == stack.peek()):
            stack.pop() #If the student at the fron gets the sandwich of their choice, then the sandwitch is removed fromt the stack
            students_without_lunch=0 #Each time a student gets the sandwich of their choice, set this value to zero so there is no cumulative addition
        else:
            queue.enqueue(student_at_front) #Enqueue the student removed from the front of the queue of they don't get the choice of their sandwich
            students_without_lunch =students_without_lunch+1
            
    output = 0

    return students_without_lunch
    

print(Simulate_Sandwitch_for_Students([1,1,0,0], [0,1,0,1]))
print(Simulate_Sandwitch_for_Students([1,1,1,0,0,1], [1,0,0,0,1,1]))
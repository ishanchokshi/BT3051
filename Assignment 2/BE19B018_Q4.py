#First create a Stack class
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
        


#The function below will return the priority number for each operand used in the infix expression
def priority(operator):
    if (operator == '-' or operator == '+'):
        return 1
    elif (operator == '*' or operator == '/' or operator == '%'):
        return 2
    elif (operator=='^'):
        return 3
    else:
        return 0
    
#The function below converts the infix expression to the postfix expression
def InfixToPostfix(infix):
    postfix = []
    stack = Stack(10000) #Create an object of the Stack class
    i = 0
    while(i <len(infix)): #Run loop till end of the expression
        if(infix[i].isdigit()):
            s=''
            while(i!=len(infix) and infix[i].isdigit()): #This will check if it is a one-digit or a two-digit number and append to the postfix expression accordingly
                s = s+infix[i]
                i=i+1
            postfix.append(s)
            continue
        elif(infix[i].isalpha()): #Will append character to the postfix expression
            postfix.append(infix[i])
            
        elif(infix[i]=='('): #Will push any opening bracket to the stack
            stack.push(infix[i])
            
        elif(infix[i]=='+' or infix[i] =='-' or infix[i]=='*' or infix[i]=='/' or infix[i]=='%' or infix[i]=='^'):
            if(not(stack.isEmpty())):
                top_in_stack = stack.peek()
                while(priority(top_in_stack)>=priority(infix[i])): #Compare the operator priorites here. 
                    postfix.append(stack.pop()) #All operators having more or same priority as "i" will be popped from the stack and appended to the postfix expression
                    if(stack.isEmpty()): 
                        break
                    else:
                        top_in_stack = stack.peek() 
                stack.push(infix[i]) #Push "i" onto stack after removing all higer and same priority operators
            else:
                stack.push(infix[i]) #If the priority order is less, then "i" will be pushed onto the stack without removing any operators
            
        elif(infix[i]==')'):
            top_in_stack = stack.peek()
            while(top_in_stack!='('):
                postfix.append(stack.pop()) #All operators above "(" will be popped out of the stack and appended to the postfix expression
                top_in_stack = stack.peek()
            stack.pop() #Pop out '(' 
                
        else:
            postfix.append(stack.pop())
        i = i+1
        
    while(not(stack.isEmpty())):
        postfix.append(stack.pop()) #Pop the remaining operators in the stack and append them to the postfix expression
                
    return postfix

#Evaluating the postfix operation
def EvaluatePostfix(ls):
    i = 0
    calc_postfix = Stack(10000) #Create another stack object from Stack class
    while (i<len(ls)):
        if(ls[i].isdigit()):
            calc_postfix.push(int(ls[i])) #Convert the operands into integer type and push them into the stack
            
        else:
            a = calc_postfix.pop() #If "i" is an operator, pop out the top two operands from the stack and do the operation on them
            b = calc_postfix.pop()
            if(ls[i]=='+'):
                result = b+a
            elif(ls[i]=='-'):
                result = b-a
            elif(ls[i]=='*'):
                result = b*a
            elif(ls[i]=='/'):
                result = b/a
            else:
                result = b**a
            calc_postfix.push(result) #Push the result of the operation into the stack
            
        i=i+1
            
    return calc_postfix.pop() #Reuturn the value of the postfix expression


s = input("Enter the infix expression: ")
postfix_exp = InfixToPostfix(s) 
value_exp = EvaluatePostfix(postfix_exp)
print("Postfix Expression: ",postfix_exp)
print("Value of Expression: ",value_exp)
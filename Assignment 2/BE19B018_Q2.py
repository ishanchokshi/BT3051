class BinaryNumber:
    def __init__(self,a):
        self.binary = a
        
    def base_10(self):
        decimal = 0
        for i in range(len(self.binary)):
            decimal = decimal + int(self.binary[i])* 2**(len(self.binary)-i-1) #Converting binary to decimal
        print("Decimal Representation: ("+str(decimal)+")"+"\u2081\u2080") #Display the decimal number with the base as its subscript
        
    def __str__(self):
        print("Binary Representation: ("+self.binary+")"+"\u2082") #Display the binary number with the base as its subscript
        self.base_10()
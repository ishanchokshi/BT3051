def decoder(encoded, n):
    """
    Add your code here.
    Remember to return the final answer.
    """
    encoded = encoded.split(" ")
    ans1 = ""
    for i in encoded:
        ls = list(i)
        strr = ""
        for j in ls:
            if(j>= "A" and j <= "Z"):
                if((ord(j)+n) <= ord("A")):
                    ans = chr(ord("Z") - ord("A") + (ord(j)+n) + 1)
                elif((ord(j)+n) >= ord("Z")):
                    ans = chr(ord("A") + (ord(j)+n) - ord("Z") - 1)        
                else: ans = chr(ord(j)+n)
            ## both if statements include code that gives cyclicity to the shift from Z-A/z-a or vice versa ##        
            if(j>= "a" and j <= "z"):
                if((ord(j)+n) <= ord("a")):
                    ans = chr(ord("z") - ord("a") + (ord(j)+n) + 1)
                elif((ord(j)+n) >= ord("z")):
                    ans = chr(ord("a") + (ord(j)+n) - ord("z") - 1)        
                else:
                    ans = chr(ord(j)+n)                            
            strr += ans  ## Adding each character to form a word after shift is done to the original character
        ans1 +=  strr ## Adding each word of the sentence once it is processed
        
        if(i!= encoded[-1]): ans1 += " " ## Creates spaces between final words
        
                     
    return ans1



if __name__ == "_main_":
    fin = open("q5_test.txt")
    data = fin.read().splitlines()
    fin.close()

    data[1] = int(data[1])
    text, n = data

    # Add your code here
    
    decoded = decoder(text,n)
    print(f'Plain: {decoded}')




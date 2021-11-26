def decoder(encoded, n):
    """
    Add your code here.
    Remember to return the final answer.
    """
    # It has been considered that no special characters existed duaring Caeser's time so they will not be considered during the decoding
    for i in encoded:
        decode_upper = lambda i,shift: (chr((ord(i) + shift - 65)% 26 + 65)) #Used to shift the uppercase letters as well as make it cyclic to ensure that special characters are not returned
        decode_lower = lambda i,shift: (chr((ord(i) + shift - 97)% 26 + 97)) #Used to shift the lowercase letters as well as make it cyclic to ensure that special characters are not returned
        if(ord(i)>=65 and ord(i)<=90):
            print(decode_upper(i,n), end = "")
        elif(ord(i)>=97 and ord(i)<=122):
            print(decode_lower(i,n), end = "")
        else:
            print(i, end ="") #To print out the spaces as it is

if __name__ == "__main__":
    fin = open("q5_test.txt")
    data = fin.read().splitlines()
    fin.close()

    data[1] = int(data[1])
    text, n = data
    decoder(data[0], data[1])
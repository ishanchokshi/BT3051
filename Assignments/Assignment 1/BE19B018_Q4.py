def prime_factors(number):
    factors = [i for i in range(2,number+1) if number%i==0] # Get all the factors of the number
    prime_factors = [] # Will be used to store all the prime factors of the number
    for j in factors:
        prime_check = [k for k in range(2,j) if j%k==0] #Get all the factors of each number in "facotrs" list except for the number itself
        if(len(prime_check)==0): #As 1 and the number itself are not included, a factor will be called prime only if it has zero elements in the "prime_check" list
            prime_factors.append(j)
            
    return list(prime_factors)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if(num>=1000000): #To ensure user in passing a number less than 10,00,000
        print("Please enter a number less than 10,00,000!")
    else:
        factors = prime_factors(num)
        print(factors)
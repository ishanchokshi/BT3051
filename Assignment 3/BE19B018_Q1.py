def min_mutations(s,t):
    """
    Calculate the minimum number of mutations required to convert one DNA sequence into another

    Parameters
    -----------
    s : String 
        Source DNA sequence
    t : String
        Target DNA sequence
    
    Returns
    -----------
    int
        The minimum number of mutations required to convert one DNA sequence into another

    >>> min_mutations('ATGC', 'ATGGG')
        5
	"""
    m = len(s)
    n = len(t)
    memo_table = [[0 for x in range(n + 1)] for x in range(m + 1)] #Creating a memoisation table to store values of subproblems
    purine = 'AG'
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                memo_table[i][j] = 2*j #Store values of the first row of the memoisation table
            elif j == 0:
                memo_table[i][j] = 2*i #Store values of the colum row of the memoisation table
            elif s[i-1] == t[j-1]:
                memo_table[i][j] = memo_table[i-1][j-1] #No additional cost required if the upper left base is same as current base
            else:
                if(s[i-1] in purine and t[i-1] in purine): #If the nucletides substituted belong to the same group(purines or pyrimidines), cost of substitution is 1 else it is 3
                    cost_substitution = 1
                else:
                    cost_substitution = 3
                memo_table[i][j] = min(memo_table[i][j-1]+2,        # Insertion
                                       memo_table[i-1][j]+2,        # Deletion
                                       memo_table[i-1][j-1]+cost_substitution)  #Substitution
    return memo_table[m][n]
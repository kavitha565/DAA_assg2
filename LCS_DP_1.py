import numpy as np

# Function to calculate the length of longest common subsequence of strings - x,y 
def LCS_length(x, y):
        m = len(x)+1
        n = len(y)+1

        #matrix used to store the length of LCS of Xi and Yj 
        c = np.zeros((m,n), dtype=int)

        #matrix used to store the directions which indicates the subproblem we used in solving LCS of Xi and Yj
        b = np.empty((m,n), dtype='U1')

        lcsLength = 0
        for i in range(1,m):
            for j in range(1,n):
                if x[i-1] == y[j-1]:
                    c[i][j] = c[i-1][j-1]+1
                    b[i][j] = "\\"
                else:
                    if c[i-1][j] >= c[i][j-1]:
                        c[i][j] = c[i-1][j]
                        b[i][j] = "^"
                    else:
                        c[i][j] = c[i][j-1]
                        b[i][j] = "<"

        lcsLength = c[m-1][n-1]

        # Display the contents of b and c matrices
        print("++++++++++++++++++++++++++++")
        print('   Y', end='   ')
        for columnHeader in list(y): 
            print(columnHeader, end='   ')
        print()
        rowHeaders = list(x)
        rowHeaders.insert(0,'X')
        for i in range(m):
            print(rowHeaders[i],end='')
            for j in range(n):
                print(b[i][j] if b[i][j] else ' ',c[i][j],end=' ')
            print()
        print("++++++++++++++++++++++++++++")

        return b,c,lcsLength

# Function used to get the LCS string
def LCS_string(b,x,m,n):
            i = m
            j = n
            lcsString = ''
            while i != 0 or j != 0:
                if b[i][j] == "\\":
                    lcsString = x[i-1]+lcsString
                    i = i-1
                    j = j-1
                elif b[i][j] == "^":
                    i = i-1
                else:
                    j = j-1
            return lcsString

def getData(fileName):
    with open(fileName, "r") as f:
        for data in f:

            x,y = data.strip().split(',')
            print('X = "'+x+'" Y = "'+y+'"')

            # Calculate the longest common subsequence of the strings
            b,c,lcsLength = LCS_length(x, y)

            # Display LCS string and length of LCS
            lcsString = LCS_string(b,x,len(x),len(y))
            print("Length of the Longest Common Subsequence is: ", lcsLength)
            print('The Longest Common Subsequence of "'+x+'" and "'+y+'" is '+lcsString)

            
# Get string values from the file
getData('LCS1.txt')


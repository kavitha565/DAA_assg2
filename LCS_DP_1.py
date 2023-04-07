import numpy as np

def LCS_length(x, y):
        m = len(x)+1
        n = len(y)+1
        c = np.zeros((m, n), dtype=int)
        b = np.empty((m, n), dtype='U1')
        lcsString = ''
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
        print(c)
        print(b)

        if lcsLength == 0:
            print("Length of the Longest Common Subsequence is: 0")
        else:
            i = m-1
            j = n-1
            while i != 0 or j != 0:
                if b[i][j] == "\\":
                    lcsString = x[i-1]+lcsString
                    i = i-1
                    j = j-1
                elif b[i][j] == "^":
                    i = i-1
                else:
                    j = j-1
            print("Length of the Longest Common Subsequence is: ", lcsLength)
            print("The Longest Common Subsequence of "+x+" and "+y+" is "+lcsString)

def getData(fileName):
    with open(fileName, "r") as f:
        x = f.readline().strip()
        y = f.readline().strip()
        return x,y

x,y = getData('LCS1.txt')
print(x,y)
LCS_length(x, y)

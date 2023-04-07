import numpy as np


def LCS_length(x, y):
    m = len(x)
    n = len(y)
    if m == 0 or n == 0:
        print("Length of the Longest Common Subsequence is: 0")
    else:
        c = np.zeros((m, n), dtype=int)
        b = np.empty((m, n), dtype='U1')
        lcsString = ''
        for i in range(m):
            for j in range(n):
                if x[i] == y[j]:
                    c[i][j] = c[i-1][j-1]+1
                    b[i][j] = "\\"
                else:
                    if c[i-1][j] >= c[i][j-1]:
                        c[i][j] = c[i-1][j]
                        b[i][j] = "^"
                    else:
                        c[i][j] = c[i][j-1]
                        b[i][j] = "<"

        i = m-1
        j = n-1
        while i != -1 or j != -1:
            if b[i][j] == "\\":
                lcsString += x[i]
                i = i-1
                j = j-1
            elif b[i][j] == "^":
                i = i-1
            else:
                j = j-1

        if len(lcsString):
            lcsString = lcsString[::-1]
        print(c)
        print(b)
        print("Length of the Longest Common Subsequence is: ", c[m-1][n-1])
        print("The Longest Common Subsequence of "+x+" and "+y+" is "+lcsString)


LCS_length('printed', 'parted')

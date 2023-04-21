Team Member 1-
Name- Rishab Khuntia
ID- 1001935008
Team Member 2-
Name- Kavitha Pasupuleti
ID- 1002044805

Language used - Python 3
IDE - Visual studio code

The flow of the code and instruction to follow while execution in mentioned below:

1. The LCS1.txt contains two strings separated by a comma(X,Y) and have multiple lines of strings.
2. Running the LCS_DP_1.py will take values from LC1.txt row wise and compute the LCS by generating the matrices - b,c. 
   The output will contain length of longest common subsequence and the LCS string of given two strings.
   The output format also contains the total time taken to execute the algorithm.
3. Run the LCS_DP_1.py and the output will be in the format:
X = "BAT" Y = "BOAT"
++++++++++++++++++++++++++++
   Y   B   O   A   T   
X  0   0   0   0   0 
B  0 \ 1 < 1 < 1 < 1 
A  0 ^ 1 ^ 1 \ 2 < 2 
T  0 ^ 1 ^ 1 ^ 2 \ 3 
++++++++++++++++++++++++++++
Length of the Longest Common Subsequence is:  3
The Longest Common Subsequence of "BAT" and "BOAT" is BAT
Time taken to find the Longest Common Subsequence is X.XXXX seconds

4. The LCS_DP_2.py will work the same as LCS_DP_1.py but the longest common subsequence will be modified in such a way that the letters will only follow an ascending order and the rest will be omitted.

5. Run the LCS_DP_2.py and the output will be in the format:
X = "BAT" Y = "BOAT"
++++++++++++++++++++++++++++
   Y   B   O   A   T   
X  0   0   0   0   0 
B  0 \ 1 < 1 < 1 < 1 
A  0 ^ 1 ^ 1 \ 2 < 2 
T  0 ^ 1 ^ 1 ^ 2 \ 3 
++++++++++++++++++++++++++++
Length of the Longest Common Subsequence is:  2
The Longest Common Subsequence of "BAT" and "BOAT" is BT
Time taken to find the Longest Common Subsequence is X.XXXX seconds


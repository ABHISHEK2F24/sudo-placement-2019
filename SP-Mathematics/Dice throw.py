/* Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.

Input: The first line of the input contains T denoting the number of test cases. First line of test case is faces 'm', number of throws 'n' and the sum to obtain 'x'.
Output: Number of ways to get sum 'x' are displayed.
Constraints:
1 <=T<= 100
1 <=m,n,x<= 50


Example:

Input: 
2
6 3 12
10 8 25

Output:
25
318648

*/




def findWays(m,n,x): 
	table=[[0]*(x+1) for i in range(n+1)] #Initialize all entries as 0 
	
	for j in range(1,min(m+1,x+1)): #Table entries for only one dice 
		table[1][j]=1
		
	for i in range(2,n+1): 
		for j in range(1,x+1): 
			for k in range(1,min(m+1,j)): 
				table[i][j]+=table[i-1][j-k]  
	
	return table[-1][-1] 
	
t = int(input())
for i in range(0,t):
    j,k,l = [int(i) for i in input().split()]
    print(findWays(j,k,l))

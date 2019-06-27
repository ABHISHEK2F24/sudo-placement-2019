/*  Calculate the angle between hour hand and minute hand.

There can be two angles between hands, we need to print minimum of two. Also, we need to print floor of final result angle. For example, if the final angle is 10.61, we need to print 10.

 

Input:

The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consists of one line conatining two space separated numbers h and m where h is hour and m is minute.

Output:
Coresponding to each test case, print the angle b/w hour and min hand in a separate line.

Constraints:

1 ≤ T ≤ 100
1 ≤ h ≤ 12
1 ≤ m ≤ 60

Example:

Input
2
9 60
3 30

Output
90
75
*/




import math
t = int(input())
for _ in range(0,t):
    h, m = [float(p) for p in input().split()]
    if m == 60:
        h = h - 1
    a = 30*h - (11/2)*m    
    a = abs(a)
    if a > 180:
        a = 360 - a
    print(math.floor(a))  

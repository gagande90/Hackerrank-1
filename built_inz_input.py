"""
This challenge is only for Python 3.

input()

In Python 3, the expression input() is equivalent to eval(input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'
Task

You are given a polynomial P of a single indeterminate (or variable), x. 
You are also given the values of x and k. Your task is to verify if P(x)=k.

Constraints 
All coefficients of polynomial P are integers. 
x and y are also integers.

Input Format

The first line contains the space separated values of x and k. 
The second line contains the polynomial P.

Output Format

Print True if P(x)=k. Otherwise, print False.

Sample Input

1 4
x**3 + x**2 + x + 1
Sample Output

True
Explanation

P(1)=13+12+1+1=4=k 
Hence, the output is True.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
i = list(map(int,input().split()))
x,k = i[0],i[1]
if input() == k:
    print True
else: print False

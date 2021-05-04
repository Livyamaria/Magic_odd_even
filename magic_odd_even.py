"""Write a program to accept an integer from the user and find the sum of digits of the number. If this sum of digits is an even number, print "Magic even", else print "Magic odd" (NOTE: Do not print the double quotes)

Input Format

The input is just one line, where the user enters an integer number

Output Format

The output is also one line, which says "Magic even" or "Magic odd", depending on the number that the user has entered.

Sample Input

56

Sample Output

Magic odd

Explanation

The user has entered the number 56. The sum of the individual digits is 5+6=11"""
n = int(input())
s = 0
l = len(str(n))
for i in range(l):
    r = n % 10
    s += r
    n = n // 10

print(s)
if s % 2 == 0:
    print("Magical even")
else:
    print("Magical odd")


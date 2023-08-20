# Exercise 1: Print First 10 natural numbers using while loop
x=1
while x<11:
    print(x)
    x+=1

# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,7):
    for j in range(1,i):
        print(j,end=' ')
    print('')

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# Expected Output:
# Enter number 10
# Sum is:  55

def sum1(ip):
    res=0
    for i in range(1,ip+1):
        res+=i
    return res

sum1(10)

# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

def multi(ip):
    res=0
    for i in range(1,11):
        res+=ip
        print(res)

multi(4)

# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected output:
# 75
# 150
# 145

def numfn(ip):
    for i in ip:
        if (i<151 and (i%5==0)):
            print(i)
        elif i>150 and i<500:
            continue
        elif i > 500:
            break

ip=[12, 75, 150, 180, 145, 525, 50]
numfn(ip)

# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5.

def nmcnt(ip):
    cnt=0
    for i in str(ip):
        cnt+=1
    return int(cnt)

nmcnt(20081996)

# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

def revptrn(ip):
    for i in range(ip,0,-1):
        for j in range(1,i+1):
            print(j,end=' ')
        print('')

revptrn(5)

# Exercise 8: Print list in reverse order using a loop
# Given:
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10

def revlst(ip):
    ip.reverse()
    for i in ip :
        print(i)

list1 = [10, 20, 30, 40, 50]
revlst(list1)

# Exercise 9: Display numbers from -10 to -1 using for loop
# Expected output:
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

for i in range(-10,0):
    print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.

# Given:

# for i in range(5):
#     print(i)
# Expected output:

# 0
# 1
# 2
# 3
# 4
# Done!

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
# Examples:
# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# Given:
# # range
# start = 25
# end = 50
# Expected output:
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47

def pnm(x,y):
    for i in range(x,y+1):
        if i in (2,3,5,7):
            print(i)
        elif i%2==0 or i%3==0 or i%5==0 or i%7==0:
            pass
        else:
            print(i)
        
pnm(25,50)

# /************
start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
# **************/

for i in range(2,29):
    if 29%i==0:
        break
else:
    print('pr')

# Exercise 12: Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

x,y=0,1
for i in range(0,10):
    print(x)
    print(y)
    x=x+y #1
    print(x)
    y=y+x
    print(y)

# /*******
# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 10 times
for i in range(10):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res
# ****************/

# Exercise 13: Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
# 120

def fct(ip):
    res=1
    for i in range(ip,0,-1):
        res*=i
    return res

fct(5)

# Exercise 14: Reverse a given integer number
# Given: 76542
# Expected output: 24567

def rvr(ip):
    return int(str(ip)[::-1])

rvr(76542)

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: list index always starts at 0
# Expected output: 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
    if i%2!=0:
        print(my_list[i])

for i in my_list[0::2]:
    print(i)

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Write a program to rint the cube of all numbers from 1 to a given number
# Given:
# input_number = 6
# Expected output:
# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

def cube(ip):
    for i in range(1,ip+1):
        print(i," ",i**3)

cube(6)

# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
# Given: # number of terms
# n = 5
# Expected output: 24690

def smn(ip):
    n='2'
    sum=0
    for i in range(1,ip+1):
        sum+=int(n*i)
    return sum

smn(5)
401951706552
# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def ptrn(ip):
    for i in range(1,ip+1):
        print('*'*i)
        if i==ip:
            for i in range(ip-1,0,-1):
                print('*'*i)

ptrn(5)
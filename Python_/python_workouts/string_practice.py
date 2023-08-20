# 1.Create a string made of the first, middle and last character

def fml(nm):
    nm=nm[0]+nm[int(len(nm)/2)]+nm[len(nm)-1]
    print(nm)

fml('ajith')#aih

fml('abarna') #ara

# 2.Create a string made of the middle three characters

def m3(nm):
    ml=int(len(nm)/2)
    nm=nm[ml-1:ml+2]
    print(nm)

m3('ajith')

m3('abarna')

# 3.Append new string in the middle of a given string
# s1= 'Ault', s2='Kelly' --> AuKellylt

def apnd_s2(s1,s2):
    nm=s1[:int(len(s1)/2)]+s2+s1[int(len(s1)/2):]
    print(nm)

apnd_s2('ajith','kumar')

apnd_s2('santhiya','ajith')

# 4.Create a new string made of the first, middle, and last characters of each input string
# s1= 'ajith',s2='santhiya' --> 'asihha'
def fml(s1,s2):
    s=s1[0]+s2[0]+s1[int(len(s1)/2)]+s2[int(len(s2)/2)]+s1[-1]+s2[-1]
    print(s)

fml('ajith','santhiya')

# 5.Arrange string characters such that lowercase letters should come first
# 'AjiTh' --> 'jihAT'

# i have added additional feature for numeric and special char. 
# order is lower,upper,num,specialchar
def lf(nm):
    li=list(nm)
    lwr=[]
    upr=[]
    num=[]
    schar=[]
    for i in range(0,len(li)):
        if li[i].islower():
            lwr.append(li[i])
        elif li[i].isupper():
            upr.append(li[i])
        elif li[i].isnumeric():
            num.append(li[i])
        else:
            schar.append(li[i])
    nm=''.join(lwr)+''.join(upr)+''.join(num)+''.join(schar)
    print(nm)

lf('AjITh')
lf('AjiTH,KUmar124k')

# 6.Count all letters, digits, and special symbols from a given string

def cntlet(nm):
    li=list(nm)
    ltr=0
    num=0
    schar=0
    for i in range(0,len(li)):
        if li[i].isalpha():
            ltr+=1
        elif li[i].isnumeric():
            num+=1
        else:
            schar+=1
    print(f"letters : {ltr}, numbers : {num}, special char : {schar}")

cntlet('Ajith@123')

# 7. Create a mixed String using the following rules

# Rule: Given two strings, s1 and s2. 
# Write a program to create a new string s3 made of the first char of s1, 
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
# Any leftover chars go at the end of the result.
# s1='abc',s2='xyz' --> 'azdycx'

def mix(s1,s2):
    ans=''
    rs2=''
    for i in s2[::-1]:
        rs2= rs2+i
    for i in range(0,len(s2)):
        ans=ans+s1[i]+rs2[i]
    print(ans)
mix('ajith','kumar')

# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter.
# s1 = 'aji' s2='ajith' => True, s1 = 'ajk' s2='ajith' => False

def chk(s1,s2):
    for i in s1:
        if i in s2:
            res = True
        else:
            res = False
            break
    return res

chk('aji','ajith')
chk('ajki','ajith')

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Given : str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome: The USA count is: 2

def occ(s1,s2):
    res = s1.upper().count(s2.upper())
    return res

occ("Welcome to USA. usa awesome, isn't it?","USA")

# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
# Given: str1 = "PYnative29@#8496"
# Expected Outcome: Sum is: 38 Average is  6.333333333333333

def sumavg(s1):
    cnt=0
    sum=0
    avg=0
    for i in s1:
        if i.isdigit():
            cnt+=1
            sum+=int(i)
        else:
            pass
    avg=sum/cnt
    print("sum is : {}, Avg is : {}".format(sum,avg))

sumavg('ajith@123')
sumavg('PYnative29@#8496')

# Exercise 10: Write a program to count occurrences of all characters within a string
# Given: str1 = "Apple"
# Expected Outcome: {'A': 1, 'p': 2, 'l': 1, 'e': 1}

def charcnt(s1):
    dic = {}
    cnt=0
    for i in s1:
        cnt=s1.count(i)
        dic[i]=cnt
    return dic

charcnt('ajiiii')

# Exercise 11: Reverse a given string
# Given: str1 = "PYnative"
# Expected Output: evitanYP

def rev(s1):
    s1=s1[::-1]
    return s1

rev('ajith')

# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
# Given: str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output: Last occurrence of Emma starts at index 43

def lstocc(s1,s2):
    s1=s1.rfind(s2)
    print("Last occurrence of Emma starts at index ",s1)
    
lstocc("ajith is ajith just ajith",'ajith')
str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2= 'Emma'
lstocc(str1,str2)

# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# Given: str1 = Emma-is-a-data-scientist
# Expected Output:
# Displaying each substring
# Emma
# is
# a
# data
# scientist

def splt(s1):
    ls=s1.split('-')
    for i in ls:
        print(i)

splt("the-name-is-ajith")

# Exercise 14: Remove empty strings from a list of strings
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

def rmvempty(l1):
    for i in l1:
        if len(i)!=0:
            l2=[i]


# Exercise 15: Remove special symbols / punctuation from a string
# Given: str1 = "/*Jon is @developer & musician"
# Expected Output: "Jon is developer musician"

def rmvspl(s1):
    s2=''
    for i in s1:
        if i.isalpha() or i.isdigit() or i.isspace():
            s2+=i
        else:
            pass
    return s2

str1 = "/*Jon is @developer & musician"
rmvspl(str1)

# Exercise 16: Removal all characters from a string except integers
# Given: str1 = 'I am 25 years and 10 months old'
# Expected Output: 2510

def rmvalpha(s1):
    s2=''
    for i in s1:
        if i.isdigit():
            s2+=i
    return int(s2)

def rmvalpha1(s1):
    s2=''.join([i for i in s1 if i.isdigit()])
    return int(s2)

str1 = 'I am 25 years and 10 months old'
rmvalpha(str1)
rmvalpha1(str1)

# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
# Given: str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output: Emma25 scientist50

def wrdnum(s1):
    ls=s1.split(' ')
    res=[]
    for i in ls:
        for j in i:
            if j.isdigit():
                res.append(i)
                break #break when first digit is encountered in work.
    return res

str1 = "Emma25 is Data scientist50 and AI Expert"
wrdnum(str1)

# /**************
temp=['ajith123','aji','steve94']
res=[]
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
res
# *****************/

# Exercise 18: Replace each special symbol with # in the following string
# Given: str1 = '/*Jon is @developer & musician!!'
# Expected Output: ##Jon is #developer # musician##

def rplspl(s1):
    for i in s1:
        if i.isalnum() or i.isspace():
            True
        else:
            s1=s1.replace(i,"#")
    return s1

str1 = '/*Jon is @developer & musician!!'
rplspl(str1)

# 19 - Output the integer number indicating the total number of occurrences of the substring in the original string.
# Sample Input
# ABCDCDC
# CDC
# Sample Output
# 2

def count_substring(string, sub_string):
    cnt=0
    lss=len(sub_string)
    for i in range(0,len(string)):
        if string[i:i+lss]==sub_string:
            cnt+=1
        else:
            pass
    return cnt

s='abcdcdc'
ss='cdc'

count_substring(s,ss)

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

# Sample Input
# qA2
# Sample Output
# True
# True
# True
# True
# True

def strchk(s):
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

strchk('qA2')

# Sample Input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
s='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
w=4
# def wrap(s,w):

len(s)-(len(s)//4)*4

loop = 

(len(s)//4)*4

for i in range(0,len(s),w):
    print(s[i:i+w])
    print(len(s[i:i+w]))

for i in range(0,26,4):
    print(i)


# Excersice 20 -
# The four values must be printed on a single line in the order specified above for each  from  to . 
# Each value should be space-padded to match the width of the binary value of  and the values should be 
# separated by a single space.
# Sample Input

# 17
# Sample Output

#     1     1     1     1
#     2     2     2    10
#     3     3     3    11
#     4     4     4   100
#     5     5     5   101
#     6     6     6   110
#     7     7     7   111
#     8    10     8  1000
#     9    11     9  1001
#    10    12     A  1010
#    11    13     B  1011
#    12    14     C  1100
#    13    15     D  1101
#    14    16     E  1110
#    15    17     F  1111
#    16    20    10 10000
#    17    21    11 10001


lnth=0
for i in range(18):
    if len(str(bin(i))) < lnth:
        lnth
    else:
        lnth=len(str(bin(i)))

for i in range(18):
    print(str(i)[2:].rjust(lnth+1)+str(oct(i)[2:]).rjust(lnth+1)+str(hex(i)[2:]).rjust(lnth+1)+str(bin(i)[2:]).rjust(lnth+1))


number=2
lnth=0
for i in range(1,number+1):
    if len(str(bin(i))) < lnth:
        lnth=lnth
    else:
        lnth=len(str(bin(i)))

for i in range(1,number+1):
    print(str(i)+str(oct(i)[2:]).rjust(lnth+1)+str(hex(i)[2:]).rjust(lnth+1)+str(bin(i)[2:]).rjust(lnth+1))

def print_formatted(number):
    # your code goes here
    lnth=0
    for i in range(1,number+1):
        if len(str(bin(i))) < lnth:
            lnth
        else:
            lnth=len(str(bin(i)[2:]))
    
    for i in range(1,number+1):
        print(str(i).rjust(lnth)+" "+str(oct(i)[2:]).rjust(lnth)+" "+str(hex(i)[2:]).upper().rjust(lnth)+" "+str(bin(i)[2:]).rjust(lnth))


print_formatted(17)

for i in range('a','z'):
    print(i)
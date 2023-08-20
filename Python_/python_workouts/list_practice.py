# Exercise 1: Reverse a list in Python
# Given: list1 = [100, 200, 300, 400, 500]
# Expected output: [500, 400, 300, 200, 100]

def revlst(ip):
    print(ip[::-1])

list1 = [100, 200, 300, 400, 500]

revlst(list1)

# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# Given:
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output: ['My', 'name', 'is', 'Kelly']

def concatlst(x,y):
    mxlen = 0
    if len(x)>=len(y):
        mxlen = len(x)
    else:
        mxlen = len(y)
    nval=''
    res=[]
    for i in range(mxlen):
        nval = x[i]+y[i]
        res.append(nval)
    return res

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

concatlst(list1,list2)

list1 = ["M", "na", "i", "Ke","jo","rev"] 
list2 = ["y", "me", "s", "lly","John"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy", "Monica"]
c = ["aji", "abi", "moni"]

x = zip(a, b,c)
print(x)
type(x)
for i in x:
    print(i)


def cnct(x,y):
    cmn=abs(len(x)-len(y))
    res=[]
    for i in range(cmn+1):
        res.append(x[i])
        res.append(y[i])
    # print(res)
    if len(x)>len(y):
        res=res+x[cmn+1:]
    else:
        res=res+y[cmn+1:]
    return res
                   
l1=[1,2,3,4,5]
l2=[6,7,8,9,10,11]

cnct(l1,l2)



# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given: numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output: [1, 4, 9, 16, 25, 36, 49]

def lstsq(ip):
    res=[]
    for i in ip:
        res.append(i**2)
    return res

numbers = [1, 2, 3, 4, 5, 6, 7]
lstsq(numbers)

# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def cclst(x,y):
    res=[]
    for i in x:
        for j in range(0,len(y)):
            res.append(i+y[j])
    return res

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
cclst(list1,list2)


# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and 
# display items from list1 in original order and items from list2 in reverse order.
# Given
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100

def mltitr(x,y):
    # print([i,j for i,j in zip(x,y)])
    for i,j in zip(x,y[::-1]):
        print(i,j,sep=" ")

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
mltitr(list1,list2)

# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# Expected output:
# ["Mike", "Emma", "Kelly", "Brad"]

def empty(x):
    for i in x:
        if i=="":
            x.remove(i)
    return x

# /**************
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# empty(list1)
y=list(filter(None,list1))
for i in filter(None,list1):
    print(i)
# ************************/

# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given: list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for i in list1:
    if isinstance(i,list):
        for j in i:

list1[2][2].append(7000)

#Excercise 8 : return second max value from list:
l = [1,2,3,4,5,6,7,7]

res = list(set(l))
res.sort(reverse=True)
res[1]

res.append(list([1,2]))
res

name,*marks='ajith 90 80 95'.split()

hash((1,2))

hash(1)+hash(2)

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    l=list(t)
    _hash = hash(l)
    print(_hash)

hash(tuple(1,2))
# 3713081631934410656

1 2
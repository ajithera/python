'''Output the desired logo.

Sample Input

5
Sample Output

    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H '''

#Replace all ______ with rjust, ljust or center. 

thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    H    
   HHH    
  HHHHH  
 HHHHHHH 
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))


#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

***********************************

'.|.'.center(27,'-')
'.|.'.ljust()


# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n,m=int(n),int(m)
n2=n//2
for i in range(1,n,2):
    print(('.|.'*i).center(m,'-'))
print('welcome'.center(m,'-'))
for i in range(n-2,-1,-2):
    print(('.|.'*i).center(m,'-'))



nums = input().split()
N, M = (int(i) for i in nums)

pattern = ".|."

k = 1
for i in range(N):
    srt_ = ""
    if i < N//2:
        print((pattern*k).center(M, "-"))
        k +=2
    elif i > N//2:
        print((pattern*k).center(M, "-"))
        k -=2
    else:
        print("WELCOME".center(M,"-"))
        k -=2

oct(10)
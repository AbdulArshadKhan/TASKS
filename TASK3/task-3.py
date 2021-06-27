def enumb(n):
    a=[]
    for i in n:
        if i%2==0:
            a.append(int(i))
    for i in a:
        print(i,end=" ")
    print('')
def onumb(n):
    b=[]
    for i in n:
        if i%2==1:
            b.append(int(i))
    for i in b:
        print(i,end=" ")
    print('')
n=input("Input :")
print("Value of n is : {}".format(n))
len1=len(n)
val=int(n)
fh=[]
sh=[]
i=len1
#print("Value of i is : {}".format(i))
while(i>(len1+1)//2):
    sh.append(val%10)
    val=val//10
    i=i-1
#print("Value of i is : {}".format(i))
while(i>0):
    fh.append(val%10)
    val=val//10
    i=i-1
fh.sort()
sh.sort()
print("First half of number is : {}".format(fh))
print("Second half of number is : {}".format(sh))
print("Even numbers in the first half are : ",end="  ")
enumb(fh)
print("Odd numbers in the first half are : ",end="  ")
onumb(fh)
print("Even numbers in the second half are : ",end="  ")
enumb(sh)
print("Odd numbers in the second half are : ",end="  ")
onumb(sh)

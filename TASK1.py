a=input("Input : ")
print("Given string is : {}".format(a))
b=[]
c=[]
d=[]
for x in a:
    if((x>='a' and x<='z') or (x>='A' and x<='Z')):
        b.append(x)
    elif(x>='0' and x<='9'):
        c.append(x)
    else:
        d.append(x)
print("Alphabets in {} are : ".format(a),end=" ")
for i in b:
    print(i,end=" ")
print('')
print("Numbers in {} are : ".format(a),end=" ")
for i in c:
    print(i,end=" ")
print('')
print("Special Characters in {} are : ".format(a),end=" ")
for i in d:
    print(i,end=" ")
print('')
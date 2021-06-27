a={}
run=True
while(run!=False):
    print("1. Add a new Contact ")
    print("2. Display all Contacts ")
    print("3. Update Contact ")
    print("4. Delete Contact ")
    print("5. Exit the application ")
    inp=int(input("\n\nEnter your choice :"))
    if(inp==1):
        name=input("\n\nEnter your name : ")
        if name in a:
            print("{} already exists \n\n".format(name))
        else:
            numb=int(input("Enter mobile number : "))
            a[name]=numb
            print("Record Added Successfully\n\n")
    elif(inp==2):
        print("\n\n")
        if(len(a)!=0):
            print("Name".center(30),end=" ")
            print("Phone number\n".center(20))
            for i in a:
                print(i.center(30),end=" ")
                print("{}".format(a[i]).center(20))
            print('\n')
        else:
            print("Contact List is Empty !! , Add Contacts \n\n")
    elif(inp==3):
        print('\n\n')
        name1=input("Enter the name :")
        if name1 in a:
            num1=input('Enter your new phone number : ')
            a[name1]=num1
            print('Phone Number Updated !\n\n')
        else:
            print('User does not Exist\n\n')
    elif(inp==4):
        name2=input('\n\nEnter the name to be deleted :')
        if name2 in a:
            a.pop(name2)
            print('Contact Deleted Successfully\n\n')
        else:
            print('User does not Exist\n\n')
    else:
        print('Thank you for using application\n\n')
        run=False

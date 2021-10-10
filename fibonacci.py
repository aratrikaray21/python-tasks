import sys
l=int(input(" Enter the limit:"))
while True:
    print("\n Select the loop using which you want to print the fibonacci series:\n 1. Using for loop\n 2. Using while loop\n 3. Exit\n")
    ch=int(input(" Enter the choice:"))
    if ch==1:
        print(" Printing the fibonacci series->")
        n1,n2=0,1
        for i in range(0,l):
            print("\t",n1)
            n=n1+n2
            n2=n1
            n1=n
    elif ch==2:
        print(" Printing the fibonacci series->")
        n1,n2=0,1
        c=0
        while c<l:
            print("\t",n1)
            n=n1+n2
            n2=n1
            n1=n
            c+=1
    elif ch==3:
        sys.exit()
    else:
        print(" Wrong choice")

import sys
l=[]
inp=int(input(" Enter the list limit:"))
j=0
print(" Enter the list elements upto limit",inp,"->")
while j in range(0,inp):
    l.append(int(input(" ")))
    j+=1
print("The original list: ",l)
while True:
    print("\n Select the loop using which you want to print the positive numbers:\n 1. Using for loop\n 2. Using while loop\n 3. Exit\n")
    ch=int(input(" Enter the choice:"))
    if ch==1:
        #Using for loop
        print(" The positive numbers in the list range:")
        for pos in l:
            if pos>=0:
                print(" ",pos, end=" ")
    elif ch==2:
        #Using while loop
        i=0
        print(" The positive numbers in the list range:")
        while i<len(l):
            if l[i]>=0:
                print(" ",l[i], end=" ")
            i+=1
    elif ch==3:
        sys.exit()
    else:
        print(" Wrong choice")

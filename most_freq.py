import sys
def most_frequent(d):
     r=[]
     for k in d:
         r.append((d[k],k))
     r.sort(reverse=True)
     for v,k in r:
         print("",k,"=",v,end=" ")
w=input(" Enter a string: ")
while True:
    print("\n Select the loop using which you want the character frequencies to be displayed->\n 1. Using for loop\n 2. Using while loop\n 3. Exit\n")
    ch=int(input(" Enter your choice:"))
    if ch==1:
        d=dict()
        for k in w:
            if k not in d:
                d[k]=1
            else:
                d[k]+=1
        most_frequent(d)
    elif ch==2:
        d=dict()
        k=0
        while k<len(w):
            if w[k] not in d:
                d[w[k]]=1
            else:
                d[w[k]]+=1
            k+=1
        most_frequent(d)
    elif ch==3:
        sys.exit()
    else:
        print(" Wrong choice")

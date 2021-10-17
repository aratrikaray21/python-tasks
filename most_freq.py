import sys
def most_frequent(w):
     d=dict()
     r=[]
     for k in w:
          if k not in d:
               d[k]=1
          else:
               d[k]+=1
     for k in d:
         r.append((d[k],k))
     r.sort(reverse=True)
     for v,k in r:
         print("",k,"=",v,end=" ")
cond=True
while cond:
     w=input(" Enter a string: ")
     print(" Displaying the letters of the entered string in the decreasing order of frequency-->")
     most_frequent(w)
     ch=input("\n Do you want to continue(y/n)?").casefold()
     if ch=='y':
          cond=True
     elif ch=='n':
          cond=False
     else:
          print("Wrong choice! Enter y for yes and n for no")

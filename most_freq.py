def most_frequent(w):
     d=dict()
     l=[]
     for k in w:
          if k not in d:
               d[k]=1
          else:
               d[k]+=1
     for k in d:
         l.append((d[k],k))
     l.sort(reverse=True)
     for v,k in l:
         print("",k,"=",v,end=" ")
condition=True
while condition:
     w=input(" Enter a string: ")
     print(" Displaying the letters of the entered string in the decreasing order of frequency-->")
     most_frequent(w)
     ch=input("\n Do you want to continue(y/n)?").casefold()
     if ch=='y':
          condition=True
     elif ch=='n':
          condition=False
     else:
          print("Wrong choice! Enter y for yes and n for no")

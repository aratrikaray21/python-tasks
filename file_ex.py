f={'py':'Python','txt':'Text','c':'C','cpp':'C++'}
file=input("Enter the file name:")
f_ex=file.split(".")
fx=f_ex[-1]
print("The file extension is:",f[fx])

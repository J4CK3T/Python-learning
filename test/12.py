test= list(input("place your numbers here:"))
a=test

def splitter(a):
    b = a[0:len(a)//2]
    c = a[len(a)//2:]
    return (b,c)

B=max(splitter(a))
C=min(splitter(a))


print("your max number from the fist half is:",max(B))
print("and your second number from the second half is",min(C))
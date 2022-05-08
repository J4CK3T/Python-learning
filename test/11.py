test=list(input("place numbers to find the answer:"))
test.sort

x1=min(test)
x1=int(x1)

x2=max(test)
x2=int(x2)

def sum(x1,x2):
    Add= x1+x2
    return Add/2

def geo_sum(x1,x2):
    prod= x1*x2
    return prod**(1/2)

print("your mean is:", sum(x1,x2))
print("your geo mean is:", geo_sum(x1,x2))

#dope done
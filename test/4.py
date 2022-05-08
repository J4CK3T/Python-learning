def suma(x1,x2,x3):
    Add= x1+x2+x3
    return Add/2

x1=int(input("place your fisrt number:"))
x2=int(input("place your second number:"))
x3=int(input("place your third number:"))

print("Your mean is as folows:",suma(x1,x2,x3))

def geo_suma(x1,x2,x3):
    Prod= x1*x2*x3
    return Prod**(1/2)

print("Your geometric mean is as folows:" ,geo_suma(x1,x2,x3))



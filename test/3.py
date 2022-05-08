def op(a,b,c):
    return (a**b)**(1/c)

a=input("input your first number:")
a=int(a)
b=input("input your second number:")
b=int(b)
c=input("input your third number:")
c=int(c)

print("result:", op(a,b,c))
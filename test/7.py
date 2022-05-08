x1=int(input("input the fisrt number:"))
x2=int(input("input your second number:"))
op=int(input("select your operation"  
    "1. +" 
    "2. -" 
    "3. *" 
    "4. /"))

def suma(x1,x2):
    sum=x1 + x2
    return sum

if op == 1:
    print("your result is:", suma(x1,x2))
elif op == 2:
    print("Nope")
elif op == 3:
    print("STOP")
elif op == 4:
    print("You violated the Law")

#it works
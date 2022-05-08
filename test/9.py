num=int(input("your number shall be checked:"))

if num > 1:
    for p in range(2, int(num/2)+1):
        if (num % p) == 0:
            print("he failed")
            break
    else:
        print("he is prime number")

#is gud
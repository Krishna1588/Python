def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
n=int(input("Enter a number:"))
print(fact(n))
n1=int(input("Enter a number:"))
print(fact(n1))
n2=int(input("Enter a number:"))
print(fact(n2))
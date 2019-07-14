s="python is very easy"
n=len(s)

print("forward direction")
i=0
while i<n:
    print(s[i],end="")
    i+=1
print()
print("Reverse Direction")
i=-1
while i>=-n:
    print(s[i],end="")
    i-=1
print()
print("Forward")
for i in s[::]:
    print(i,end="")
print()
print("Reverse")
for i in s[::-1]:
    print(i,end="")




n1=int(input("enter first number="))
n2=int(input("enter second number"))
b=0;
if n1<0:
    n1=0-n1
if n2<0:
    n2=0-n2
for i in range (1,n1) and range (1,n2):
    m=n1%i
    k=n2%i
    if m==0:
        j=i
    if k==0:
        l=i
    if j==l:
        if j>b:
            b=j
print(b)


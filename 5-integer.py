num=int(input("Enter the limit"))
a=[]
for i in range(num):
    k=(int(input("Enter the number")))

    if k<100:
        a.append(k)
    else:
        a.append("over")
print(a)

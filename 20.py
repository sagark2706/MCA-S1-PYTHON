num1=[2,10,3,7,6,8,4,9]
num2=[]
m=len(num1)
for i in range(m):
    if num1[i]%2!=0:
        num2.append(num1[i])
num1=num2
print(num1)



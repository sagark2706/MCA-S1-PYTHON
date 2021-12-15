n1 = []
n2 = []
s1 = 0
s2 = 0
a = 0
b = 0
ln1=int(input("Enter the limit of first list"))
for i in range(ln1):
    a=(int(input("Enter the number")))
    n1.append(a)
    s1 = s1+a
print("Sum of first list element",s1)
ln2=int(input("Enter the limit of second list"))
for j in range(ln2):
    b=int(input("Enter the number"))
    n2.append(b)
    s2 = s2 + b
print("sum of second list elements",s2)
if ln1 == ln2:
    input("Elements are same")
else:
    print("Not same")
for i in range(ln1):
    for j in range(ln2):
       if n1[i] == n2[j]:
        print(n1[i])

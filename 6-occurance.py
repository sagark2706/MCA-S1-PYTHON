n=int(input("Enter the limit"))
a=[]
l=[]
for i in range(n):
    k=input("Enter the Names")
    l=k.split()[0]

    if 'a' in l:
       a.append(l)
print(a)

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
d1={"name":"sagar","age":20}
d2={"gender":"male","course":"MCA"}
print(Merge(d1,d2))


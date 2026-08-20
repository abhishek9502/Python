nums=list(map(int,input("Enter Numbers here :").split(",")))
result=[]
for i in nums:
    if i>10:
        result.append(i)
print(result)
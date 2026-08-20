nums=list(map(int,input("Enter Numbers here :").split(",")))
dic={}
for i in nums:
    dic[i]=dic.get(i,0)+1
count=0
for i in dic.values():
    if i>=2:
        count+=1
print(count)
    
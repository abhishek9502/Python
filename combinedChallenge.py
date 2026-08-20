nums=[10,25,30,45,50,75,90,100]
result=[]
for i in nums:
    if i>30 and i%5==0 and i!=75:
        result.append(i)
print(result)
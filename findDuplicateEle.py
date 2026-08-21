nums=[10,20,30,10,40,50,20]
duplicates=set()
seen=set()
for i in nums:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)
print(duplicates)


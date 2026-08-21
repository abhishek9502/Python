nums=[1,2,4,9,11,0,12]
maxi=float("-inf")
mini=float("inf")
for i in nums:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print(f"Maximum value is : {maxi}")
print(f"Minimum value is : {mini}")

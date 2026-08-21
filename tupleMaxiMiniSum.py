nums=(1,2,3,4,5,6)
sum=0
maxi=float("-inf")
mini=float("inf")
for i in nums:
    sum+=i
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print(f"Sum of the number are: {sum}")
print(f"Maximum value is: {maxi}")
print(f"Minimum value is: {mini}")
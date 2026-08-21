nums=[1,2,3,4,5,6,0,9,10,11]
maxi=float("-inf")
second_maxi=float("-inf")
for i in nums:
    if i>maxi:
        second_maxi=maxi
        maxi=i
    elif i>second_maxi and i<=maxi:
        second_maxi=i
print(second_maxi)

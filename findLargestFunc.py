def find_largest(numbers):
    maxi=float("-inf")
    for i in numbers:
        if i>maxi:
            maxi=i
    return maxi
print(find_largest([1,2,3,4,5,6]))
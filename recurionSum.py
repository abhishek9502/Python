n=int(input("Enter Number :"))
def sumOFNumbers(n):
    if n==1:
        return n
    return n+sumOFNumbers(n-1)
print(sumOFNumbers(n))
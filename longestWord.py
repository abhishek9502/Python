s=input("Enter sentence here :")
words=s.split()
var=words[0]
for i in range(1,len(words)):
    if len(var)<len(words[i]):
        var=words[i]
print(var)
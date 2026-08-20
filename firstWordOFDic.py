words=input("enter the sequence :")
words=words.split()
print(words)
var=words[0]
for i in range(len(words)-1):
    if var.upper()<words[i+1].upper() :
        var=words[i]
print(var)


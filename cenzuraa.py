a=str(input())
b=str(input())
a=a.split(', ')
c=b
b=b.split()
for i in a:
    for k in b:
        if i in k:
            y='*'*len(i)
            c=c.replace(i,y)
print(c)

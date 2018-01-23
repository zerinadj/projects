l=[] #List of words user inputs
s=str(input())
n=len(s)
l.append(s)
for i in range(n-1):
    x=str(input())
    l.append(x)

sve='' #All words will be in this string
y='' #This will be 'column' word
for k in l:
    for j in k:
        sve=sve+j
lista=[] #All column words will be in this list
for c in range(len(s)):
    for r in range(c,len(sve),n):
        y=y+sve[r]
    lista.append(y)
    y=''
for m in lista:
    for b in m:
        print(b.upper(), end=' ')
    print('')
if l==lista:
    print('True')
else:
    print('False')

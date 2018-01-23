a=str(input())
b=str(input())
a=a.lower()
b=b.lower()
a=a.replace(' ','')
b=b.replace(' ','')
lista1=[]
lista2=[]
for i in range(len(a)):
    lista1.append(a[i])
for j in range(len(b)):
    lista2.append(b[j])
lista1.sort()
lista2.sort()
if lista1==lista2:
    print('Anagrami su')
else:
    print('Nisu')

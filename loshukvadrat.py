mat=[]
lista=[]
for i in range(3):
    mat.append([])
    for j in range(3):
        x=int(input())
        if x in lista:
            x=int(input('Enter new number, this one is already in list'))
        if x>0 and x<10 and x not in lista:
            mat[i].append(x)
        lista.append(x)
sum1=0
sum2=0
sum3=0
sum4=mat[0][2]+mat[1][1]+mat[2][0]
for r in range(3):
    sum1=sum1+mat[0][r]
    sum2=sum2+mat[r][0]
    sum3=sum3+mat[r][r]
if sum1==sum2==sum3==sum4:
    print('Lo Shu')
else:
    print('False')

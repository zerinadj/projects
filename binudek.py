n=int(input())
dek=0
i=0
while n!=0:
    cifra=n%10
    dek=dek+cifra*(2**i)
    n=n//10
    i=i+1
print(dek)

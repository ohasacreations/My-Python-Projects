N1=int(input())
N2=int(input())
x=0
while(N1>=N2):
    if(N1%2==0):
        x=x+N1
    N1=N1+1
print(x)
def Binary(N):
    bn=""
    while(N>0):
        Rem=N%2
        N=N//2
        bn=str(Rem)+bn
    return bn
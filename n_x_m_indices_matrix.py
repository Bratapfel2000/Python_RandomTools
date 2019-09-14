#prints matrix with indices m x n 


def matrix_(m,n):
    for m in range(1,m+1):
        for n in range(1,n+1):
            dx = "d"+str(m)+str(n)
            print(dx)



matrix_(4,5)

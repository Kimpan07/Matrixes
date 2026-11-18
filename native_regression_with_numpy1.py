from numpy import *
import matplotlib.pyplot as plt


def powers(list,n1,n2):
    M=[]
    for k in range(len(list)):
        new_row=[]
        for i in range(n1,n2+1):
            new_row.append(list[k]**i)
        M.append(new_row)
    return array(M)


def native_regression_with_numpy(fil):
    M=loadtxt(fil)
    A=transpose(M)
    X=A[0]
    Y=A[1]
    Xp= powers(A[0],0,1)
    Yp= powers(A[1],1,1)
    Xpt= transpose(Xp)
    [[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    Y2=[]
    for x in X:
        Y2.append(b+m*x)
    plt.plot(X,Y,'ro')
    plt.plot(X,Y2)
    plt.show() 

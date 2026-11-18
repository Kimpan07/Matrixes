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



def poly(a,x):  #a är lista på koefficienter medans x är det x värde vi vill räkna ut vad det blir för
    y=0
    for i in range(len(a)):
        y=y+a[i]*x**i
    return y

    



def numpy_regression(fil, n): #filnamn och n=grad på polynom
    M=loadtxt(fil)
    A=transpose(M)
    X=A[0]
    Y=A[1]
    Xp= powers(A[0],0,n)
    Yp= powers(A[1],1,1)
    Xpt= transpose(Xp)
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    a = a[:,0]
    
    X2=linspace(min(X),max(X),int((max(X)-min(X))/0.2))

    Y2=[]
    for i in range(len(X2)):
        Y2.append(poly(a,X2[i]))
    
    
    plt.plot(X,Y,'ro')
    plt.plot(X2,Y2)
    plt.show() 

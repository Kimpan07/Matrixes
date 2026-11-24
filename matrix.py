def transpose(matrix):
    M=[]
    if len(matrix)==0:
        return M
    else:
        for i in range(len(matrix[0])):
            new_row=[]
            for j in range(len(matrix)):
                new_row.append(matrix[j][i])
            M.append(new_row)
        return M
# print(transpose([[9,3,2,1],[4,7,4,1],[3,6,4,8]]))



def powers(list,n1,n2):
    M=[]
    for k in range(len(list)):
        new_row=[]
        for i in range(n1,n2+1):
            new_row.append(list[k]**i)
        M.append(new_row)
    return M

#print(powers([2,3,4],0,2))




def matmul(A,B):
    M=[]
    if len(A)==0 or len(B)==0:
        return M
    else:
        if len(A[0])==len(B):
            for i in range(len(A)):
                new_row=[]
                for j in range(len(B[0])):
                    s=0
                    for k in range(len(A[0])):
                        s=s+A[i][k]*B[k][j] 
                    new_row.append(s)
                M.append(new_row)
            return M
        else:
            print("Matrix multiplication not possible, give a well defined matrix multiplication.")

#s1=[[1,2,3],[4,5,6]]
#s2=[[7,8],[9,10],[11,12]]

#print(matmul(s1,s2)) #ska blir [[58,64],[139,154]]



#Endast 2x2 matriser funkar här

def invert(matrix):
    det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    M=[]
    new_row=[]
    new_row.append(matrix[1][1]/det)
    new_row.append(-1*matrix[0][1]/det)
    M.append(new_row)
    new_row=[]
    new_row.append(-1*matrix[1][0]/det)
    new_row.append(matrix[0][0]/det)
    M.append(new_row)
    return M




def loadtxt(fil):
    table=[]
    with open(fil) as file:
        for line in file:
            table.append([x for x in line.split()])
    return table

            

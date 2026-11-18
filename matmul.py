def matmul(A,B):
    M=[]
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

s1=[[1,2,3],[4,5,6]]
s2=[[7,8],[9,10],[11,12]]

print(matmul(s1,s2)) #ska blir [[58,64],[139,154]]
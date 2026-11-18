def transpose(matrix):
    M=[]
    for i in range(len(matrix[0])):
        new_row=[]
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        M.append(new_row)
    return M
# print(transpose([[9,3,2,1],[4,7,4,1],[3,6,4,8]]))
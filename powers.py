def powers(list,n1,n2):
    M=[]
    for k in range(len(list)):
        new_row=[]
        for i in range(n1,n2+1):
            new_row.append(list[k]**i)
        M.append(new_row)
    return M

print(powers([2,3,4],0,2))

point={1:0,2:0.8415,3:0.5,4:2}

def liniar(p1,p2, x,point):
    f = (( point[p1]-point[p2])/(p1-p2))*x +(p1*point[p2]-p2*point[p1])/(p1-p2)
    return f
def polinomit(point,x):

    matrix =[[0 for j in range(len(point))]for i in range(len(point))]
    print(matrix)
    keys = list(point.keys())
    print(keys)
    for j in range(len(point)):
        for i in range(len(point)):
            if j == 0:
                matrix[i][0] = 1
            else:
                matrix[i][j] = pow(keys[i],j)
    print(matrix)


polinomit(point,1)




r1=int(input("r1"))
c1=int(input("c1"))
r2=int(input("r2"))
c2=int(input("c2"))
if r1==r2 and c2==c1:
    m1=[]
    m2=[]
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(int(input("enter element")))
        m1.append(row)
    for i in range(r2):
        row=[]
        for j in range(c2):
            row.append(int(input("enter elements")))
        m2.append(row)

    result=[]
    print("add of the matrix")
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(m1[i][j]+m2[i][j])
        result.append(row)
    print(result)
else:
    print("not possbli")

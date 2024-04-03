r1=int(input("r1"))
c1=int(input("c1"))
m1=[]
m2=[]
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input("enter element")))
    m1.append(row)
for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(m1[j][i])
        m2.append(row)
print(m2)

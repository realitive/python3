from Check import Matrix
A = Matrix(3,3)
B = Matrix(2,2)
print("A")
A.display()
print("B")
B.display()
print("Result = A + B")
C = A + B
if C != 1:
    C.display()
print("Result= A - B")
D = A - B
if D != 1:
    D.display()
E = A * 2
print("Result = A * 2")
if E != 1:
    E.display()
print("Result = A * B")
F = A * B
if F != 1:
    F.display()
A.trans()
print("A^T")
A.display()
detA = A.det()
if detA != 'string':
    print("Det A = " + str(detA))

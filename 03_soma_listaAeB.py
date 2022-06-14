A = []
B = list()
C = []

for c in range(20):
  y = int(input())
  A.append(y)

for c in range(20):
  w = int(input())
  B.append(w)

for c in range(20):
  C.append((A[c]+B[c]))

print(A)
print(B)
print(C)
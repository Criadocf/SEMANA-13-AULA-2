def contador(lista,b):
  repetido = 0
  for c in lista:
    if b == c:
      repetido += 1
  return repetido

y = 1
lista1 = list()
while y != 0:
  y = int(input())
  if y !=0:
    lista1.append(y)

def main():
    w = int(input())
    ch = contador(lista1, w)
    print(lista1)
    print(w)
    print(ch)

if __name__=='__main__':
    main()


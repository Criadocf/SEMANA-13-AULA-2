nome = list()
idades = list()
alturas = list()

def media_func(n):
  m = 0
  for c in n:
    m += c
  return m/len(n)


for c in range(3):
  nome.append(str(input()))
  idades.append(int(input()))
  alturas.append(float(input()))


ch = media_func(alturas)



print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for c in range(3):
  alturas1 = alturas[c]
  if alturas1 < ch:
    if idades[c] > 13:
      print(nome[c])
      print(ch)
      print(alturas1)

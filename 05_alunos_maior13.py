nome = list()
idades = list()
alturas = list()

def media_func(n):
  m = 0.0
  for c in n:
    m += c
  return round(m/len(n), 2)


for c in range(30):
  nome.append(str(input()))
  idades.append(int(input()))
  alturas.append(float(input()))

ch = media_func(alturas)
print('MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
for c in range(30):
  alturas1 = alturas[c] #CRIO ESSA VARIAVEL alturas1 PRA RECEBER OS VALORES DA LISTA alturas.
  if alturas1 < ch and idades[c] > 13:
    print(nome[c])




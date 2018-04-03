##exercicio 1
l = list(input("Escreva uma frase: "))
print(l)
tamanho = len(l)

dicionario = {}

for i in range(tamanho):
    dicionario[l[i]] = l.count(l[i])

print(dicionario)
print("---------------------")

##exercicio 2
r = input("Escreva uma frase: ")
s = input("Escreva uma frase: ")
if s in r:
    print(r.find(s[0]))
print("---------------------")

##exercicio 3
r = input("Escreva uma frase: ")
s = input("Escreva uma frase: ")
i = 0
t = []

if len(r)>len(s):
  for i in range (len(s)):
     if s[i] in r:
          t.append(s[i])
elif len(s)>len(r):
  for i in range (len(r)):
     if r[i] in s:
          t.append(s[i])
a = "".join(t)
print(t)
print("---------------------")

##exercicio 4
r = input("Escreva uma frase: ")
s = input("Escreva uma frase: ")
i = 0
t = []

if len(r)>len(s):
  for i in range (len(r)):
     if r[i] not in s:
          t.append(r[i])
elif len(s)>len(r):
  for i in range (len(s)):
     if s[i] not in r:
          t.append(s[i])
a = "".join(t)
print(t)



    


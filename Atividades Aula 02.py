
# coding: utf-8

# In[2]:


cigDia = int(input("Quantos cigarros você fuma por dia? "))
ano = int(input("Por quantos anos você fuma? "))
cigarros = (365*ano)*cigDia
perdaVida = 10*cigarros
totalDias = perdaVida/1440
print("O total de dias que você perdeu até agora foi: %d" %totalDias)


# In[3]:


x=int(input("Escreva um valor inteiro entre 1 e 10: "))
y=int(input("Escreva outro valor inteiro entre 1 e 10: "))
soma=x+y
if soma<8:
    media=(x+y)/2
    print(media)
if soma==8:
    produto=x*y
    print(produto)
if soma>8:
    if x>y:
        div=x/y
    else:
        div=y/x
    print(div)


# In[13]:


a=float(input("Digite o valor A: "))
b=float(input("Digite o valor B: "))
c=float(input("Digite o valor C: "))
    

if a<(b+c):
    if b<(a+c):        
        if c<(a+b):
            if a==b==c:
                print("É um triângulo equilátero!")
            if (a==b!=c):
                print("É um triângulo isóceles!")
            if (a==c!=b):
                print("É um triângulo isóceles!")
            if (b==c!=a):
                print("É um triângulo isóceles!")
            if(a!=b!=c):
                print("É um triângulo escaleno!")
        else: 
            print("Não é um triângulo")
    else: 
        print("Não é um triângulo")
else:
    print("Não é um triângulo")  
    


# In[ ]:


count=0
while count>=0:
    num=int(input("Digite um número INTEIRO: "))
    if(num>0):
        print("Esse número é positivo")
    if(num<0):
        print("Esse número é negativo")
    if(num==0):
        print("Esse número é igual a zero")
    count+=1


# In[12]:


i=1
s=0
for i in range(1,51):
    s += (2*i-1)/i
    i+=1
print("O somatório é %d" %s)


# In[3]:


num=int(input("Digite um número inteiro positivo: "))
s=0
cont=0
while num>0:
    s+=num
    cont+=1
    num=int(input("Digite um número inteiro positivo: "))
print(s/cont)


# In[12]:


num = 0
soma_par = 0
soma_impar = 0 
n_par = 0
n_impar = 0

print ("Digite 10 números inteiros: ")
for n in range(1,11):
    num = int(input("Digite o nº %d: " %n))
    if num % 2 == 0:
        soma_par += num
        n_par += 1
    else:
        soma_impar += num
        n_impar += 1
print("Quantidade de números pares lidos: %d" %n_par)
print("Quantidade de números ímpares lidos: %d" %n_impar)
print("Soma de números pares lidos: %d" %soma_par)
print("Média dos números ímpares lidos: %.2f" %(float(soma_impar)/float(n_impar)))


# In[ ]:


num=int(input("Digite um numero: "))
div=0
for div in range(1, num):
    if num % div == 0:
        div += 1
        if div > 1:
            break
if div<=2:
  print("É primo")
else:
  print("Não é primo")


# In[21]:


n=int(input("Digite um número: "))
c=n
f=1
while c>0:
    f*=c
    c-=1
print(f)


# In[ ]:


for i in range (1,11):
    n=int(input("Digite um número: "))
    c=n
    f=1
    while c>0:
        f*=c
        c-=1
    print(f)


# In[3]:


a = int(input("Digite um número inteiro A: "))
b = int(input("Digite um número inteiro B: "))
if a<b:
    for i in range(a,b+1):
        print(i)
elif a>b:
    for i in range(b, a+1):
        print(i)
else: 
    print(a)


# In[7]:


s=0
num = int(input("Digite um número inteiro: "))
for n in range(1, 100):
    if n==1:
        s=1
        cont=1
    s+=1/(n*3)
    cont+=1
    if num==cont:
        print(s)


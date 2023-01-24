################################################# 
## Autor: Edgard Simas                          #
## Este programa faz calculos entre dois números# 
#################################################

#Variáveis
num1 = 8
num2 = 4

soma = num1+num2  #8+4
sub = num1-num2   #8-4
multi = num1*num2 #8*2
div =  num1/num2  #8/4  

print("######################")
print("# Calculadora Básica #")
print("# Entre dois inteiros#")
print("######################")


print("O resulatdo da soma é:",soma)
print("O resulatdo da subtração é:", sub)
print("O resulatdo da multiplicação é:",multi)
print("O resulatdo da divisão é:",div)



import time
time.sleep(2)
t0 = time.time()
for i in range(10000000):
    pass

t1 = time.time()
print(t1 - t0)
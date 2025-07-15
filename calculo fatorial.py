# funcao de calc
def calculofatorial(n):
 resultado = 1
 for i in range(1,n+ 1):
         resultado = resultado*i
 return resultado

#inicio sistema 
n=int(input('digite um numero '))  
fatorial = calculofatorial(n)
print('o seu fatorial é',fatorial)
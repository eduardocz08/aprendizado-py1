## Escrevendo em um arquivo

with open('repository/nomes.txt', 'w') as arquivo:
     arquivo.write('Eduardo\nGuilherme\nDaniel')

# Lendo o conteúdo do arquivo
with open ('nomes.txt','r') as arquivo:
     for linha in arquivo:
          print(linha.strip())




import csv
#gravar dados em csv
with open ('alunos.csv', 'w' , newline="") as arquivo:
     escritor = csv.writer (arquivo)
     escritor.writerow ({'nome', 'nota'})
     escritor.writerow ({'Ana', 8.5})
     escritor.writerow ({'Carlos', 6.7})

with open ('alunos.csv', 'r') as arquivo:
     for linha in arquivo:
          print (linha)
     
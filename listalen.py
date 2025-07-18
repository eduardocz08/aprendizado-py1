def media_lista (lista):
    if len(lista) == 0:
        return 0
    
    soma =sum(lista)
    quantidade = len(lista)

    media = soma / quantidade

    return media

print(media_lista([10, 20, 30]))
entrada = input('digite os numeros separados por espaço:')

lista =[int(x)for x in entrada.split()]

resultado =media_lista(lista)

print (f'a media dos numeros é:{resultado}')
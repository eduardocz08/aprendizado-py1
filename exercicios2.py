import datetime

def agenda_inteligente():
    nome= input ('Olá! Qual é o seu nome?')

    data_str = input ('Digite sua data de nascimento (formato DD/MM/AAAA):')


    try:
        data_nasc = datetime.datetime.strptime (data_str, '%d/%m/%Y')


        dias_semana = ['segunda-feira', 'terça-feira','quarta-feira','quinta-feira', 'sexta-feira','sábado', 'domingo']
        
        
        
        indice_dia = data_nasc.weekday()
        dia_semana = dias_semana [indice_dia]
        
        
        print (f'\nOlá, {nome}!Você nasceu em uma {dia_semana}.')
    
    except ValueError:
        print('Data inválida. Certifique-se de usar o formato DD/MM/AAAA.')


agenda_inteligente()

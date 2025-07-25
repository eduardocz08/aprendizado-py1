def converter_temperature():
    entrada = input('Digite a temperatura (ex: 32C ou 100F): ').strip().lower()

    if entrada.endswith('c') or entrada.endswith('f'):
        unidade = entrada[-1]
        valor_str = entrada[:-1]

        try:
            valor = float(valor_str)

            if unidade == 'c':
                fahrenheit = (valor * 9/5) + 32
                print(f'{valor:.2f}°C equivalem a {fahrenheit:.2f}°F')

            elif unidade == 'f':
                celsius = (valor - 32) * 5/9
                print(f'{valor:.2f}°F equivalem a {celsius:.2f}°C')

            else:
                print('Unidade inválida. Use "C" para Celsius ou "F" para Fahrenheit.')

        except ValueError:
            print('Valor numérico inválido. Tente novamente com um número, ex: 25C ou 77F.')
    else:
        print('Formato inválido. Use algo como "25C" ou "77F".')

# Chamada da função
converter_temperature()
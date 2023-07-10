def binario_para_decimal(binario):
    decimal = 0
    for digito in binario:
        decimal = decimal * 2 + int(digito)
    return decimal

def octal_para_decimal(octal):
    decimal = 0
    for digito in octal:
        decimal = decimal * 8 + int(digito)
    return decimal

def hexadecimal_para_decimal(hexadecimal):
    decimal = 0
    for digito in hexadecimal:
        if digito.isdigit():
            decimal = decimal * 16 + int(digito)
        else:
            decimal = decimal * 16 + ord(digito.upper()) - ord('A') + 10
    return decimal

def main():
    while True:
        opcao = input("****Sistema de conversão****\n(1) Binário\n(2) Octal\n(3) Hexadecimal\n(0) Sair\nDigite a opção desejada: ")

        if opcao == '1':
            binario = input("Digite o número binário: ")
            print("Valor inserido:", binario)
            decimal = binario_para_decimal(binario)
            print("Decimal:", decimal)
        elif opcao == '2':
            octal = input("Digite o número octal: ")
            print("Valor inserido:", octal)
            decimal = octal_para_decimal(octal)
            print("Decimal:", decimal)
        elif opcao == '3':
            hexadecimal = input("Digite o número hexadecimal: ")
            print("Valor inserido:", hexadecimal)
            decimal = hexadecimal_para_decimal(hexadecimal)
            print("Decimal:", decimal)
        elif opcao == '0':
            confirmacao = input("Tem certeza que deseja sair? (S/N): ")
            if confirmacao.upper() == 'S':
                print("Programa finalizado.")
                break
            else:
                continue
        else:
            print("Opção inválida! Por favor, tente novamente.")

if __name__ == '__main__':
    main()

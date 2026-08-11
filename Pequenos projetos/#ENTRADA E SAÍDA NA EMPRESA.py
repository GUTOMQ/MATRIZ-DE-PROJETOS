#Dicionário de contas com matrícula e senha
contas: dict[int, int] = {
    10: 1023,
    20: 2045,
    30: 3067,
    40: 4089,
}

hr_chegada: str = ""
hr_almoco: str = ""
hr_retorno: str = ""
hr_saida: str = ""
opcao: int = 0
temp_chegada: str = ""
temp_almoco: str = ""
temp_retorno: str = ""
temp_saida: str = ""


#Login com validação de 5 tentativas
tentativas = 0
while tentativas < 5:
    matricula = int(input("Digite sua matrícula: "))
    if matricula not in contas:
        tentativas += 1
        print("Matrícula inválida.")
        continue

    senha = int(input("Digite sua senha: "))
    if senha != contas[matricula]:
        tentativas += 1
        print("Senha incorreta.")
        continue

    break

if tentativas >= 5:
    print("Número máximo de tentativas excedido. Saindo do sistema...")
    opcao = 6
else:
    print("Login bem-sucedido.")

# Loop para bater o ponto
while opcao != 6:
    opcao = int(input("Digite 1 para Cadastrar Chegada, 2 Almoço, 3 Retorno, 4 Saída, 5 Ver Registros de Ponto, 6 sair: "))
    if opcao == 1:
        hr_chegada = input("Digite o horário de chegada: ")
        if temp_chegada == hr_chegada:
            print("Horário de chegada já batido. Digite outro horário.")
        if hr_chegada > "09:00":
            print("Não permitido, contatar o RH.")
        else:
            print("Horário de chegada batido com sucesso.")
            temp_chegada = hr_chegada
    
    elif opcao == 2:
        hr_almoco = input("Digite o horário do almoço: ")
        if hr_chegada == "":
            print("Digite a chegada antes de bater o almoço.")
        elif hr_almoco < "11:00" or hr_almoco > "14:00":
            print("Horário de almoço inválido. Digite um horário entre 11:00 e 14:00.")
        elif temp_almoco == hr_almoco:
            print("Horário de almoço já batido. Digite outro horário.")
        else:
            print("Horário de almoço batido com sucesso.")
            temp_almoco = hr_almoco
    
    elif opcao == 3:
        hr_retorno = input("Digite o horário de retorno: ")
        if temp_retorno == hr_retorno:
            print("Horário de retorno já batido. Digite outro horário.")
        if temp_almoco == "11:00" and hr_retorno < "12:00":
            print("Intervalo menor que 1 hora. Aguarde completar o intervalo")
            if temp_almoco == "12:00" and hr_retorno < "13:00":
                print("Intervalo menor que 1 hora. Aguarde completar o intervalo")
                if temp_almoco == "13:00" and hr_retorno < "14:00":
                    print("Intervalo menor que 1 hora. Aguarde completar o intervalo")
                    if temp_almoco == "14:00" and hr_retorno < "15:00":
                        print("Intervalo menor que 1 hora. Aguarde completar o intervalo")
        else:
            print("Horário de retorno batido com sucesso.")
            temp_retorno = hr_retorno
    
    elif opcao == 4:
        hr_saida = input("Digite o horário de saída: ")
        if temp_saida == hr_saida:
            print("Horário de saída já batido. Digite outro horário.")
        if temp_almoco == "" or temp_retorno == "":
            print("Não Permitido, Contatar o RH.")
        else:
            print("Horário de saída batido com sucesso.")
            temp_saida = hr_saida
    
    elif opcao == 5:
        print("Registros de ponto:")
        print(f"Chegada: {temp_chegada}")
        print(f"Almoço: {temp_almoco}")
        print(f"Retorno: {temp_retorno}")
        print(f"Saída: {temp_saida}")

    else:
        print("Opção inválida. Digite um número de 1 a 6.")

print("Saindo do sistema...")
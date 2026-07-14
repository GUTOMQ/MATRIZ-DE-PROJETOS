# Cadastro de Venda

print("=" * 50)
print("        CADASTRO DE VENDA")
print("=" * 50)

# Entrada de dados
id_venda = input("ID da Venda: ")
data = input("Data (dd/mm/aaaa): ")
vendedor = input("Nome do Vendedor: ")
cliente = input("Nome do Cliente: ")
produto = input("Produto: ")
categoria = input("Categoria: ")

quantidade = int(input("Quantidade: "))

# 1ª condição, se o usuário digitar acima de 100 em quantidade, não vai ter em estoque
# 2ª condição, se for à vista tem desconto de 5%, e à prazo vai somar + 5% do valor
# Verifica estoque
if quantidade > 100:
    print("\n❌ Estoque insuficiente!")
    print("A quantidade solicitada excede o estoque disponível (100 unidades).")
else:
    preco_unitario = float(input("Preço Unitário (R$): ").replace(",", "."))

    # Valor da compra
    valor_total = quantidade * preco_unitario

    # Forma de pagamento
    print("\nForma de pagamento")
    print("1 - À vista (5% de desconto)")
    print("2 - A prazo (+5% de acréscimo)")

    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        desconto = valor_total * 0.05
        valor_final = valor_total - desconto
        forma_pagamento = "À vista"
    elif opcao == "2":
        acrescimo = valor_total * 0.05
        valor_final = valor_total + acrescimo
        forma_pagamento = "A prazo"
    else:
        print("Opção inválida!")
        exit()

    # Extrato
    print("\n" + "=" * 50)
    print("           EXTRATO DA COMPRA")
    print("=" * 50)

    print(f"ID da Venda.....: {id_venda}")
    print(f"Data............: {data}")
    print(f"Vendedor........: {vendedor}")
    print(f"Cliente.........: {cliente}")
    print(f"Produto.........: {produto}")
    print(f"Categoria.......: {categoria}")
    print(f"Quantidade......: {quantidade}")
    print(f"Preço Unitário..: R$ {preco_unitario:.2f}")
    print(f"Valor Bruto.....: R$ {valor_total:.2f}")
    print(f"Pagamento.......: {forma_pagamento}")

    if opcao == "1":
        print(f"Desconto........: R$ {desconto:.2f}")
    else:
        print(f"Acréscimo.......: R$ {acrescimo:.2f}")

    print(f"Valor Final.....: R$ {valor_final:.2f}")
    print("=" * 50)
    print("Obrigado pela compra!")
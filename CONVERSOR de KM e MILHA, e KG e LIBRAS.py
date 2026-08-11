#CONVERSOR (simples) de KM e MILHA, e KG para LIBRAS 
print("1 - km para milhas")
print("2 - kg para libras")

opcao = int(input("Escolha: "))

if opcao == 1:
    km = float(input("Digite os km: "))
    print("Milhas:", km * 0.621371)

if opcao == 2:
    kg = float(input("Digite os kg: "))
    print("Libras:", kg * 2.20462)
unidade = input("Digite a unidade (cm, m ou km): ").lower()
valor = float(input("Digite o valor: "))

if unidade == "cm":
    cm = valor
elif unidade == "m":
    cm = valor * 100
elif unidade == "km":
    cm = valor * 100000
else:
    print("Unidade inválida!")
    exit()

m = cm / 100
km = cm / 100000
milhas = cm / 160934.4

print("\nResultado:")
print(f"Centímetros: {cm:.2f} cm")
print(f"Metros: {m:.2f} m")
print(f"Quilômetros: {km:.5f} km")
print(f"Milhas: {milhas:.6f} mi")
def inverter(entrada):
    string_invertida = ""
    for i in range(len(entrada) - 1, -1, -1):
        string_invertida += entrada[i]
    return string_invertida

entrada = input("Informe uma string: ")

resultado = inverter(entrada)

print(f"String invertida: {resultado}")

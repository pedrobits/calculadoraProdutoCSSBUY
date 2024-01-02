def coletarGramasProduto():
    while True:
        try:
            gramas = int(input("Por favor, informe a quantidade de gramas do produto: "))
            if gramas >= 0:
                return gramas
            else:
                print("Por favor, insira um valor válido (não negativo).")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
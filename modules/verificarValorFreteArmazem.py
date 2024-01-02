def coletarValorFreteArmazem():
    valorFreteParaArmazem = 5

    while True:
        try:
            novoValorFrete = int(input(
                f"Qual o valor do frete para o envio ao armazém: "))
            
            print(f"O novo valor do frete para o envio ao armazém é de {novoValorFrete}¥")
            
            verificacaoValorFrete = input("O Valor está correto? (s/n): ").lower()

            if verificacaoValorFrete == "s":
                return novoValorFrete
            elif verificacaoValorFrete == "n":
                print("Digite o novo valor novamente.")
            else:
                print("Por favor, selecione uma opção válida (s/n).")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
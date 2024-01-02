from modules.consultar_TaxaEnvio import consultar_taxaEnvio
from modules.verificarValorFreteArmazem import coletarValorFreteArmazem
from modules.coletarGramasProduto import coletarGramasProduto
from modules.obterTaxaCambio import obterTaxaCambio

# Pergunta ao usuário o preço do produto em USD
preco_produto_usd = float(input("Digite o preço do produto em USD: "))

FreteParaArmazem = coletarValorFreteArmazem()
gramas = coletarGramasProduto()
CambioYuan, CambioDolar = obterTaxaCambio()

if CambioYuan is not None and CambioDolar is not None:
    print(f"A taxa de câmbio do dólar é: {CambioDolar}")
    print(f"A taxa de câmbio do yuan é: {CambioYuan}")
else:
    print("Não foi possível obter as taxas de câmbio.")

if CambioDolar and CambioYuan:
    # Transforma o preço do produto de USD para BRL usando a taxa de câmbio
    preco_produto_brl = preco_produto_usd * float(CambioDolar)

    taxa_envio_usd = float(consultar_taxaEnvio(gramas))
    taxa_envio_brl = taxa_envio_usd * float(CambioDolar)
    taxa_envioArmazem_brl = FreteParaArmazem * float(CambioYuan)

    custo_total = taxa_envio_brl + preco_produto_brl + taxa_envioArmazem_brl
    
    margem_lucro = 0.50
    preco_venda_ideal = custo_total * (1 + margem_lucro)

    print(f"\nO preço do produto em USD é: ${preco_produto_usd:.2f}")
    print(f"O preço do produto em BRL é: R${preco_produto_brl:.2f}")
    print(f"A taxa de envio para o Brasil é de R${taxa_envio_brl:.2f}")
    print(f"O custo total, incluindo o produto e o envio tanto para o Armazem quanto para o Brasil, é de R${custo_total:.2f}")
    
    print(f"O preço ideal de venda (com uma margem de lucro de 50%) é R${preco_venda_ideal:.2f}")
else:
    print("Não foi possível obter a taxa de câmbio.")

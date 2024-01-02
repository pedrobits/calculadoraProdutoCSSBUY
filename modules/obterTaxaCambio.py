import requests

def obterTaxaCambio():
    try:
        # Obter a taxa de câmbio do dólar (USD)
        api_url_usd = "http://economia.awesomeapi.com.br/json/last/USD-BRL"
        response_usd = requests.get(api_url_usd)
        response_usd.raise_for_status()
        CambioDolar = response_usd.json()["USDBRL"]["ask"]

        # Obter a taxa de câmbio do yuan (CNY)
        api_url_cny = "https://economia.awesomeapi.com.br/json/last/CNY-BRL"
        response_cny = requests.get(api_url_cny)
        response_cny.raise_for_status()
        CambioYuan = response_cny.json()["CNYBRL"]["ask"]

        return CambioYuan, CambioDolar
    except requests.exceptions.RequestException as err:
        print(f"Erro ao obter as taxas de câmbio: {err}")
        return None, None

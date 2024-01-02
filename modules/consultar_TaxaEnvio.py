from playwright.sync_api import sync_playwright
import time


def consultar_taxaEnvio(gramas):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            permissions=[
                'geolocation', 'notifications']
        )
        page = context.new_page()
        page.set_default_timeout(10000)

        timeout = 5000
        page.set_default_timeout(timeout)

        page.goto('https://www.cssbuy.com/?go=page&action=estimates')

        campoPeso = page.locator('#weight')
        campoPeso.fill(str(gramas))

        selecionarPais = page.locator('#area')
        selecionarPais.select_option('29')

        time.sleep(3)

        confirmarSimulacao = page.locator('#submit')
        confirmarSimulacao.click()

        campoPrecoEnvio = page.locator(
            '#result > table > tbody > tr:nth-child(3) > td:nth-child(3)')

        texto_elemento = campoPrecoEnvio.text_content()

        precoemDolardoEnvio = float(texto_elemento.split('≈')[-1][1:])

        # Imprime o valor
        print(f"O valor para FJ-BR-EXP-F é: ${precoemDolardoEnvio}")

        browser.close()

        return precoemDolardoEnvio

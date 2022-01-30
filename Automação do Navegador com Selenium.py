
# Instalar e/ou importar Bibliotecas
import pandas as pd
pd.set_option('display.max_columns', 500)
from IPython.display import display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome(r"C:\Users\Nathalia Maciel\chromedriver.exe")

# Lógica
# Coletar informações a respeito da cotação do Dólar
navegador.get("https://www.google.com.br")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)

# Coletar informações a respeito da cotação do Euro
navegador.get("https://www.google.com.br")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Coletar informações a respeito da cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".")
print(cotacao_ouro)
navegador.quit()

# Atualizar base de dados
df = pd.read_excel(r"C:\Users\Nathalia Maciel\Desktop\Aulas Python\Intensivão 3\Produtos.xlsx")
df.loc[df["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
df.loc[df["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
df.loc[df["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
df["Preço de Compra"] = df["Preço Original"] * df["Cotação"]
df["Preço de Venda"] = df["Preço de Compra"] * df["Margem"]
# print(df)

# Exportar base de dados
df.to_excel("Produtos(1).xlsx", index=False)


# Importar bibliotecas
# pyautogui
# pyperclip
# pandas
# numpy
# openpyxl

import pandas as pd
import pyautogui
import time
import pyperclip

# Lógica do trabalho

# Passo 1: abrir Excel de Vendas
df = pd.read_excel(r"C:\Users\Nathalia Maciel\Desktop\Aulas Python\Intensivão 1\Vendas - Dez.xlsx")
print(df)

# Passo 2: analisar relatório de vendas (somar faturamento e quantidades)
faturamento = df["Valor Final"].sum()
quantidade = df["Quantidade"].sum()
print("faturamento")

# Passo 3: enviar e-mail com a informação
pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=775, y=428, clicks=2)
pyperclip.copy("https://outlook.office.com/mail/")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=192, y=174)
time.sleep(1.5)
pyautogui.write("edson.barbosa@seugil.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas - 15_01_2022")
pyautogui.hotkey("ctrl","v")
pyautogui.press("tab")
texto = f"""Prezados colegas,

Segue faturamento do dia: R${faturamento:,.2f}
E também a soma das quantidades: {quantidade:,}

Abs,
Edson Barbosa."""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")

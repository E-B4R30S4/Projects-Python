
# Intalar e/ou Importar Bibliotecas
import plotly.express as px
import pandas as pd

# Lógica
# Importar base de dados
# Tratamento de dados
#   exclua dados inúteis (df = df.drop(["coluna"], axis=1/0)
#   trate valores reconhecidos de forma errada (df["c/l strong"] = pd.to_numeric(df["c/l strong"], errors="coerce"))
#   trate valores vazios (df = df.dropna(how="all/any", axis=1/0)
# Análise básica de dados
# Análise detalhada dos dados (por gráficos/fig)
#   racional: para cada (for) coluna (variável) no (in) df (tabela) faça (:)
#   racional: se (if) a coluna (variável) for diferente (!=) a coluna x ("")
#   racional: fig (gráfico) = px.histogram (tipo de gráfico)(tabela, eixo x, diferenciação de cores)

df = pd.read_csv(r"C:\Users\Nathalia Maciel\Desktop\Aulas Python\Intensivão 2\telecom_users.csv")
df = df.drop(["Unnamed: 0"], axis=1)
df["TotalGasto"] = pd.to_numeric(df["TotalGasto"], errors="coerce")
df = df.dropna(how="all", axis=1)
df = df.dropna(how="any", axis=0)
# print(df.info())

# print(df["Churn"].value_counts())
# print(df["Churn"].value_counts(normalize=True).map("{:.2%}".format))

for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color="Churn")
        fig.show()

# Conclusões e insights
#   Pessoas com núcleo familiar menor têm mais chances de cancelar (churn)
#       a) podemos criar um plano família
#   Estamos perdendo muitos clientes nos primeiros meses
#       a) tem alguma ação promocional que tá trazendo muito cliente desqualificado
#       b) podemos pensar em dar bônus para o cliente nos primeiros meses
#       c) a primeira experiência do cliente pode não ser positiva
#   Estamos com um problema na Fibra
#   Quanto mais serviços o cliente tem, menor a chance de cancelar
#       a) a gente pode criar uma promoção oferencendo serviços grátis ou a preço baixo
#   Quase todo o cancelamento está no contrato mensal
#       a) dar desconto no contrato anual
#   Evitar boleto eletrônico como forma de pagamento
#       a) vamos dar desconto nas outras opções

import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime

# Conectar ao banco de dados
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estoque_db"
)
# Consulta para obter o valor total da compra por mês referente
query = "SELECT DATE_FORMAT(data_compra, '%Y-%m') AS mes_referente, SUM(preco_compra * quantidade_estoque) AS total_gasto FROM produtos GROUP BY mes_referente"
cursor = connection.cursor()
cursor.execute(query)
resultados = cursor.fetchall()
cursor.close()

# Separar os resultados em listas de meses e valores gastos
meses = [resultado[0] for resultado in resultados]
valores_gastos = [resultado[1] for resultado in resultados]

# Criar um gráfico de barras na horizontal para representar os valores gastos por mês
plt.figure(figsize=(10, 5))
plt.barh(meses, valores_gastos, color='blue')  # Coluna verde
plt.title("Valor Gasto por Mês")
plt.xlabel("Valor Gasto")
plt.ylabel("Mês de Referência")
plt.grid(axis='x')

# Anotar os valores no gráfico
for i, v in enumerate(valores_gastos):
    plt.text(v, i, str(v), va='center', color='white', fontweight='bold')

# Definir o fundo como preto
plt.gca().set_facecolor('white')

plt.show()

# Fechar a conexão com o banco de dados
connection.close()
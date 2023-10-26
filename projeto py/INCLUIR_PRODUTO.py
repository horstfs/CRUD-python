import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estoque_db"
        )
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

# Função para criar um novo produto
def criar_produto():
    nome = entry_nome.get()
    marca = entry_marca.get()
    preco_compra = entry_preco_compra.get()
    preco_venda = entry_preco_venda.get()
    data_compra = entry_data_compra.get()
    quantidade_estoque = entry_quantidade_estoque.get()

    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO produtos (nome, marca, preco_compra, preco_venda, data_compra, quantidade_estoque)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (nome, marca, preco_compra, preco_venda, data_compra, quantidade_estoque))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Produto criado com sucesso!")

        # Limpa os campos de entrada após a inserção
        limpar_campos()
        atualizar_lista()

# Função para ler produtos
def ler_produtos():
    conexao = conectar_bd()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conexao.close()
        return produtos
    else:
        return []

# Função para atualizar a lista de produtos
def atualizar_lista():
    lista_produtos.delete(*lista_produtos.get_children())
    produtos = ler_produtos()
    for produto in produtos:
        lista_produtos.insert("", "end", values=produto)

# Função para limpar os campos de entrada
def limpar_campos():
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    entry_marca.delete(0, tk.END)
    entry_preco_compra.delete(0, tk.END)
    entry_preco_venda.delete(0, tk.END)
    entry_data_compra.delete(0, tk.END)
    entry_quantidade_estoque.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Gerenciador de Produtos")

# Cabeçalho da lista de produtos
lista_produtos = ttk.Treeview(root, columns=("ID", "Nome", "Marca", "Preço Compra", "Preço Venda", "Data Compra", "Quantidade Estoque"))
lista_produtos.heading("ID", text="ID")
lista_produtos.heading("Nome", text="Nome")
lista_produtos.heading("Marca", text="Marca")
lista_produtos.heading("Preço Compra", text="Preço Compra")
lista_produtos.heading("Preço Venda", text="Preço Venda")
lista_produtos.heading("Data Compra", text="Data Compra")
lista_produtos.heading("Quantidade Estoque", text="Quantidade Estoque")

# Preencher a lista de produtos inicialmente
produtos = ler_produtos()
for produto in produtos:
    lista_produtos.insert("", "end", values=produto)

lista_produtos.pack(padx=10, pady=10)

# Botão para atualizar a lista
btn_atualizar_lista = ttk.Button(root, text="Atualizar Lista", command=atualizar_lista)
btn_atualizar_lista.pack(pady=5)

# Campos de edição
frame_edicao = ttk.LabelFrame(root, text="Editar Produto")
frame_edicao.pack(padx=10, pady=10)

label_id = ttk.Label(frame_edicao, text="ID:")
entry_id = ttk.Entry(frame_edicao, state="disabled")

label_nome = ttk.Label(frame_edicao, text="Nome:")
entry_nome = ttk.Entry(frame_edicao)

label_marca = ttk.Label(frame_edicao, text="Marca:")
entry_marca = ttk.Entry(frame_edicao)

label_preco_compra = ttk.Label(frame_edicao, text="Preço Compra:")
entry_preco_compra = ttk.Entry(frame_edicao)

label_preco_venda = ttk.Label(frame_edicao, text="Preço Venda:")
entry_preco_venda = ttk.Entry(frame_edicao)

label_data_compra = ttk.Label(frame_edicao, text="Data Compra:")
entry_data_compra = ttk.Entry(frame_edicao)

label_quantidade_estoque = ttk.Label(frame_edicao, text="Quantidade Estoque:")
entry_quantidade_estoque = ttk.Entry(frame_edicao)

label_id.grid(row=0, column=0, padx=5, pady=5)
entry_id.grid(row=0, column=1, padx=5, pady=5)

label_nome.grid(row=1, column=0, padx=5, pady=5)
entry_nome.grid(row=1, column=1, padx=5, pady=5)

label_marca.grid(row=2, column=0, padx=5, pady=5)
entry_marca.grid(row=2, column=1, padx=5, pady=5)

label_preco_compra.grid(row=3, column=0, padx=5, pady=5)
entry_preco_compra.grid(row=3, column=1, padx=5, pady=5)

label_preco_venda.grid(row=4, column=0, padx=5, pady=5)
entry_preco_venda.grid(row=4, column=1, padx=5, pady=5)

label_data_compra.grid(row=5, column=0, padx=5, pady=5)
entry_data_compra.grid(row=5, column=1, padx=5, pady=5)

label_quantidade_estoque.grid(row=6, column=0, padx=5, pady=5)
entry_quantidade_estoque.grid(row=6, column=1, padx=5, pady=5)

# Botão para criar um produto
btn_criar = ttk.Button(frame_edicao, text="Criar Produto", command=criar_produto)
btn_criar.grid(row=7, columnspan=2, pady=5)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import styles


produtos = []   #lista para os produtos

def salvar():
    nome = valornome.get()
    quantidade = valorquantidade.get()
    preco = valor.get()     #atribui os valores digitados à variaveis

    if nome and quantidade.isdigit() and preco.replace('.', '', 1).isdigit():  # isdigit = verifica se as strings sao validas // preco.replace('.', '', 1).isdigit() -> pode ser um numero decimal ex: 22.34 substitui o ponto por ''
        produtos.append({"nome": nome, "quantidade": int(quantidade), "preco": float(preco)}) #classe produto   -> adiciona um produto a lista produtos[]
        atualizarquadro()
        valornome.delete(0, tk.END)
        valorquantidade.delete(0, tk.END)
        valor.delete(0, tk.END) #limpa os campos depois que o usuario insere um valor
    else:
        messagebox.showerror("Erro", "Dados inválidos.")

def atualizarquadro():
    quadroprodutos.config(state="normal")  # habilita temporariamente para edição
    quadroprodutos.delete("1.0", tk.END)  # apaga o conteúdo do input

    for produto in produtos:
        quadroprodutos.insert(tk.END, f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}\n")

    quadroprodutos.config(state="disabled")  # desabilita para impedir edições manuais


# Criar janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")
root.geometry("600x400")
root.configure(bg=styles.BG_COLOR)
root.bind('<Return>', lambda event: salvar()) #permitir que o enter funcione para o automatizador

#root -> base da janela

# Labels e Entradas
tk.Label(root, text="Nome:", **styles.LABEL_STYLE).place(x=20, y=20) #herda do css
valornome = tk.Entry(root, **styles.ENTRY_STYLE) #input text
valornome.place(x=120, y=20)

tk.Label(root, text="Quantidade:", **styles.LABEL_STYLE).place(x=20, y=60)
valorquantidade = tk.Entry(root, **styles.ENTRY_STYLE)
valorquantidade.place(x=120, y=60)

tk.Label(root, text="Preço:", **styles.LABEL_STYLE).place(x=20, y=100)
valor = tk.Entry(root, **styles.ENTRY_STYLE)
valor.place(x=120, y=100)

# Botões
registrar = tk.Button(root, text="Registrar", command=salvar, **styles.BUTTON_STYLE)
registrar.place(x=20, y=140)

sair = tk.Button(root, text="Fechar", command=root.quit, **styles.BUTTON_STYLE)
sair.place(x=120, y=140)

# Área de exibição de produtos
quadroprodutos = tk.Text(root, width=40, height=15, **styles.TEXT_STYLE, state="disabled")
quadroprodutos.place(x=280, y=20)

root.mainloop() #inserir varios produtos rodando uma vez



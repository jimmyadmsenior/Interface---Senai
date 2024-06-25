import customtkinter
from tkinter import messagebox, Entry, Text, simpledialog
from datetime import date

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("600x600")
janela.title("Autoescola Conceição")
    
num_cadastros = 0
cadastros = []

def clicar_login():
    global num_cadastros, cadastros
    nome_usuario = campo_nome.get()
    data_nascimento = campo_data_nascimento.get()
    cpf_usuario = campo_cpf.get()
    email_usuario = campo_email.get()

    hoje = date.today()
    ano_nascimento, mes_nascimento, dia_nascimento = map(int, data_nascimento.split('/'))
    data_nascimento_obj = date(dia_nascimento, mes_nascimento, ano_nascimento)
    idade = hoje.year - data_nascimento_obj.year - ((hoje.month, hoje.day) < (data_nascimento_obj.month, data_nascimento_obj.day))

    if idade < 18:
        messagebox.showerror("NÃO APTO", "Você não está apto a tirar a carteira de motorista pois é menor de 18 anos.")
    else:
        if num_cadastros >= 20:
            messagebox.showerror("Limite Excedido", "O limite de 20 cadastros já foi atingido. Por favor, entre em contato com a Autoescola Conceição.")
        else:
            print(f"Usuário: {nome_usuario}, Data de Nascimento: {data_nascimento}, CPF: {cpf_usuario}, Email: {email_usuario}")
            messagebox.showinfo("LOGIN", "Login efetuado com sucesso! Você está apto para tirar sua carteira de motorista em nossa Autoescola.")
            cadastros.append((nome_usuario, data_nascimento, cpf_usuario, email_usuario))
            num_cadastros += 1

def abrir_suporte():
    mensagem_suporte = campo_mensagem_suporte.get()
    if mensagem_suporte.strip() == "":
        messagebox.showerror("Erro", "Por favor, digite uma mensagem de suporte.")
    else:
        messagebox.showinfo("Suporte ao Cliente", f"A seguinte mensagem foi enviada:\n\n{mensagem_suporte}")
        campo_mensagem_suporte.delete(0, "end")

def abrir_historia():
    messagebox.showinfo("História da Empresa", "A Autoescola Conceição foi fundada em 1995 com o objetivo de fornecer educação de trânsito de qualidade para a comunidade local. Ao longo dos anos, nos tornamos uma referência em treinamento de motoristas na região, mantendo nosso compromisso com a segurança e excelência no serviço.")

def abrir_visualizar_cadastros():
    senha = simpledialog.askstring("Senha de Administrador", "Digite a senha de administrador:")
    if senha == "DevsSquad":
        if num_cadastros > 0:
            cadastros_str = "\n".join([f"Usuário: {nome}, Data de Nascimento: {data_nascimento}, CPF: {cpf}, Email: {email}" for nome, data_nascimento, cpf, email in cadastros])
            messagebox.showinfo("Cadastros", cadastros_str)
        else:
            messagebox.showinfo("Cadastros", "Nenhum cadastro realizado ainda.")
    else:
        messagebox.showerror("Acesso Negado", "Senha de administrador incorreta.")

titulo = customtkinter.CTkLabel(janela, text="Autoescola Conceição", font=("Arial", 18, "bold"))
titulo.pack(padx=20, pady=20)

campo_nome = customtkinter.CTkEntry(janela, placeholder_text="Seu nome")
campo_nome.pack(padx=20, pady=10)

campo_data_nascimento = customtkinter.CTkEntry(janela, placeholder_text="Data de nascimento")
campo_data_nascimento.pack(padx=20, pady=10)

campo_cpf = customtkinter.CTkEntry(janela, placeholder_text="CPF")
campo_cpf.pack(padx=20, pady=10)

campo_email = customtkinter.CTkEntry(janela, placeholder_text="Email")
campo_email.pack(padx=20, pady=10)

campo_mensagem_suporte = customtkinter.CTkEntry(janela, placeholder_text="Mensagem de suporte")
campo_mensagem_suporte.pack(padx=20, pady=10)

lembrar_login = customtkinter.CTkCheckBox(janela, text="Lembrar login")
lembrar_login.pack(padx=20, pady=10)

btn_login = customtkinter.CTkButton(janela, text="Efetuar Login", command=clicar_login)
btn_login.pack(padx=20, pady=10)

btn_suporte = customtkinter.CTkButton(janela, text="Enviar Mensagem de Suporte", command=abrir_suporte)
btn_suporte.pack(padx=20, pady=10)

btn_historia = customtkinter.CTkButton(janela, text="Ver História da Empresa", command=abrir_historia)
btn_historia.pack(padx=20, pady=10)

btn_visualizar_cadastros = customtkinter.CTkButton(janela, text="Visualizar Cadastros", command=abrir_visualizar_cadastros)
btn_visualizar_cadastros.pack(padx=20, pady=10)

janela.mainloop()

# Jimmy Alessandro de Castilho 🤑

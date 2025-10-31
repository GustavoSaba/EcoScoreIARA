import customtkinter as ctk
import requests
import pywinstyles as pwstyles
from tkinter import messagebox
from model.config_model.config import API_URL, BG_LOGIN, PROFILE, PASSWORD, EMAIL
from PIL import Image

def iniciar_gui():
    login_app = ctk.CTk()
    login_app.title("EcoScore - Login")
    login_app.geometry("1093x626")
    login_app.resizable(False, False)
    ctk.set_appearance_mode("light")

    def fazer_login():
        cod_empresa = entry_cod.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if not cod_empresa or not email or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            response = requests.post(
                API_URL,
                params={
                    "cod_empresa": cod_empresa,
                    "empresa_email": email,
                    "empresa_senha": senha
                }
            )
            if response.status_code == 200:
                data = response.json()
                messagebox.showinfo(
                    "Sucesso",
                    f"Login realizado!\nEmpresa: {data['empresa_email']}"
                )
            else:
                erro = response.json().get("detail", "Erro desconhecido.")
                messagebox.showerror("Erro", erro)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao conectar com o servidor: {e}")

    def cadastro():
        print("Indo para o cadastro")

    frame = ctk.CTkFrame(login_app)
    frame.pack(expand=True, fill="both", pady=40)

    frame.pack_propagate(False)

    bg_verde = ctk.CTkImage(Image.open(BG_LOGIN), size=(1094, 546))
    bg_label = ctk.CTkLabel(frame, image=bg_verde, text="")
    bg_label.place(relx=0.5, rely=0.5, anchor="center")

    text_left = ctk.CTkFrame(
        frame,
        fg_color='#000001',
        bg_color='#000001'
    )
    text_left.place(relx=0.125, rely=0.27, relwidth=0.23, relheight=0.4)

    card = ctk.CTkFrame(
        frame, 
        #width=454, 
        #height=438, 
        corner_radius=12,
        bg_color='#000001',
        fg_color="#FFFAFA"
    )
    card.place(relx=0.55, rely=0.10, relwidth=0.4153, relheight=0.8)
    #card.pack(pady=(66, 42))

    #titulo = ctk.CTkLabel(card, text="Login EcoScore", font=("Arial", 22, "bold"))
    #titulo.pack(pady=20)
    seu_login = ctk.CTkLabel(
        text_left, 
        text="Faça seu Login", 
        font=("Poppins", 32, "bold"), 
        text_color="white",
        width=254,
        height=43
        )
    seu_login.pack(fill="x")

    bem_vindo = ctk.CTkLabel(
        text_left, 
        text="Bem vindo de volta!", 
        font=("Poppins", 14), 
        text_color="#CEE2B3",
        width=140,
        height=16
        )
    bem_vindo.pack(pady=12)

    btn_cadastro = ctk.CTkButton(
        text_left,
        corner_radius=12,
        width=157,
        height=56,
        text="CADASTRE-SE",
        font=("Poppins", 14, "bold"),
        text_color="#FFFAFA",
        fg_color="#000001",
        bg_color="#000001",
        border_width= 2,
        border_color="#FFFAFA",
        hover_color="#A8AC96",
        command=cadastro
    )
    btn_cadastro.pack(side="bottom")
    pwstyles.apply_style(btn_cadastro, "acrylic")

    entry_cod = ctk.CTkEntry(
        card,
        corner_radius=12,
        width=380,
        height=55,
        border_width=0,
        fg_color='#F3EBEB',
        placeholder_text="Código da Empresa",
        placeholder_text_color='#74866E',
        font=('Poppins', 20),
        text_color="#747C71",
        justify="center"
    )
    #entry_cod.place(rely=0.13)
    entry_cod.pack(anchor='center', pady=(58, 16))

    entry_email = ctk.CTkEntry(
        card,
        corner_radius=12,
        width=380,
        height=55,
        border_width=0,
        fg_color='#F3EBEB',
        placeholder_text="Email", 
        placeholder_text_color='#74866E',
        font=('Poppins', 20),
        text_color="#747C71",
        justify="center"
    )
    entry_email.pack(anchor='center', pady=16)

    entry_senha = ctk.CTkEntry(
        card,
        corner_radius=12,
        width=380,
        height=55,
        border_width=0,
        fg_color='#F3EBEB',
        placeholder_text="Senha", 
        show="*",
        placeholder_text_color='#74866E',
        font=('Poppins', 20),
        text_color="#747C71",
        justify="center"
    )
    entry_senha.pack(anchor='center', pady=16)

    font_botao = ctk.CTkFont(family="Poppins", size=30, weight="bold")

    btn_login = ctk.CTkButton(
        card,
        corner_radius=12,
        width=293,
        height=45,
        text="ENTRAR",
        font=font_botao,
        text_color="#FFFAFA",
        fg_color="#8ECD87",
        hover_color="#7A9B56",
        command=fazer_login
    )
    btn_login.pack(pady=(16, 58))

    profile = ctk.CTkImage(Image.open(PROFILE), size=(16, 19))
    profile_label = ctk.CTkLabel(entry_cod, image=profile, text="")
    profile_label.place(relx=0.05, rely=0.2)

    password = ctk.CTkImage(Image.open(PASSWORD), size=(16, 19))
    password_label = ctk.CTkLabel(entry_senha, image=password, text="")
    password_label.place(relx=0.05, rely=0.2)

    email = ctk.CTkImage(Image.open(EMAIL), size=(16, 19))
    email_label = ctk.CTkLabel(entry_email, image=email, text="")
    email_label.place(relx=0.05, rely=0.2)

    pwstyles.set_opacity(card, 1, '#000001')
    pwstyles.set_opacity(text_left, 1, '#000001')
    #pwstyles.set_opacity(btn_cadastro, 1, '#000001')

    login_app.mainloop()

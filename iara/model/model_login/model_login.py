import customtkinter as ctk
import requests
from tkinter import messagebox

API_URL = "http://127.0.0.1:8000/login"

def iniciar_gui():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    app = ctk.CTk()
    app.title("EcoScore - Login")
    app.geometry("400x350")

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

    frame = ctk.CTkFrame(app)
    frame.pack(pady=40, padx=30, fill="both", expand=True)

    titulo = ctk.CTkLabel(frame, text="Login EcoScore", font=("Arial", 22, "bold"))
    titulo.pack(pady=20)

    entry_cod = ctk.CTkEntry(frame, placeholder_text="Código da Empresa", width=250)
    entry_cod.pack(pady=10)

    entry_email = ctk.CTkEntry(frame, placeholder_text="Email", width=250)
    entry_email.pack(pady=10)

    entry_senha = ctk.CTkEntry(frame, placeholder_text="Senha", show="*", width=250)
    entry_senha.pack(pady=10)

    btn_login = ctk.CTkButton(
        frame,
        text="Entrar",
        fg_color="green",
        hover_color="#006400",
        command=fazer_login,
        width=200
    )
    btn_login.pack(pady=20)

    app.mainloop()

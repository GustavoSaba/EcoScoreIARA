import customtkinter as ctk
import requests
from session import current_user
from tkinter import messagebox
from model.config_model.config import API_URL

def iniciar_gui_perguntas():
    perguntas_app = ctk.CTk()
    perguntas_app.title("Ecoscore - Perguntas")
    perguntas_app.geometry("1093x626")
    perguntas_app.resizable(False, False)
    perguntas_app.config(bg="#FFFAFA")
    ctk.set_appearance_mode("light")

    lista_perguntas = []
    indice_pergunta_atual = 0

    def exibir_pergunta():
        nonlocal indice_pergunta_atual

        if indice_pergunta_atual >= len(lista_perguntas):
            canvas.itemconfig(id_texto_pergunta, text="Fim do questionário!")
            canvas.itemconfig(id_texto_pergunta_completa, text="")

            btn_sim.configure(state="disabled")
            btn_nao.configure(state="disabled")
            return

        pergunta_atual = lista_perguntas[indice_pergunta_atual]
        num_pergunta = pergunta_atual.get('cod_pergunta')
        texto_pergunta = pergunta_atual.get('pergunta_texto', 'Texto não encontrado.')
        total_perguntas = len(lista_perguntas)

        canvas.itemconfig(id_texto_pergunta, text=f"{num_pergunta}/{total_perguntas}")
        canvas.itemconfig(id_texto_pergunta_completa, text=texto_pergunta)

    def responder(resposta_texto):
        nonlocal indice_pergunta_atual
        
        pergunta_atual = lista_perguntas[indice_pergunta_atual]
        cod_pergunta_fk = pergunta_atual.get('cod_pergunta')

        payload = {
            "cod_empresa_FK": current_user.cod_empresa,
            "cod_pergunta_FK": cod_pergunta_fk,
            "respDiaria_texto": resposta_texto # Será "1" ou "0"
        }

        try:
            btn_sim.configure(state="disabled")
            btn_nao.configure(state="disabled")

            response = requests.post(f"{API_URL}/resposta/", params=payload)

            if response.status_code == 200:
                btn_sim.configure(state="normal")
                btn_nao.configure(state="normal")

                indice_pergunta_atual += 1
                exibir_pergunta()
            else:
                erro = response.json().get("detail", "Erro desconhecido.")
                messagebox.showerror("Erro ao Responder", f"Não foi possível registrar a resposta: {erro}")

                btn_sim.configure(state="normal")
                btn_nao.configure(state="normal")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Erro de Conexão", "Não foi possível conectar ao servidor.")
            btn_sim.configure(state="normal")
            btn_nao.configure(state="normal")
        except Exception as e:
            messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
            btn_sim.configure(state="normal")
            btn_nao.configure(state="normal")

    def preencher_perguntas():
        nonlocal lista_perguntas
        try:
            response = requests.get(f"{API_URL}/perguntas/")
            if response.status_code == 200:
                dados_api = response.json()
                lista_perguntas = dados_api.get('perguntas', [])
                if not lista_perguntas:
                    canvas.itemconfig(id_texto_pergunta, text="Nenhuma pergunta encontrada.")
                    return
                
                indice_pergunta_atual = 0
                exibir_pergunta()
            else:
                print(f"Erro ao buscar perguntas: {response.status_code}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    frame = ctk.CTkFrame(perguntas_app, width=1093, height=626, corner_radius=0)
    frame.pack(expand=True, fill="both")
    frame.pack_propagate(False)

    canvas = ctk.CTkCanvas(frame, highlightthickness=0, bg='#FFFAFA')
    canvas.pack(fill='both', expand=True)

    id_texto_pergunta = canvas.create_text(503, 127, text='Carregando...', font=("Inter", 48, 'bold'), fill='#4E5D4D')
    id_texto_pergunta_completa = canvas.create_text(503, 200, text='Carregando...', font=("Inter", 18), fill='#4E5D4D', width=800)

    btn_sim = ctk.CTkButton(perguntas_app, text="SIM", width=150, height=50, font=("Inter", 20, "bold"), fg_color="#7EB87E", command=lambda: responder("1"))
    btn_nao = ctk.CTkButton(perguntas_app, text="NÃO", width=150, height=50, font=("Inter", 20, "bold"), fg_color="#E74C3C", command=lambda: responder("0"))

    canvas.create_window(503 - 80, 350, window=btn_sim, anchor="center")
    canvas.create_window(503 + 80, 350, window=btn_nao, anchor="center")

    perguntas_app.after(100, preencher_perguntas)
    perguntas_app.mainloop()
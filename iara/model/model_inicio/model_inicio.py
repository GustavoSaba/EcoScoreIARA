import customtkinter as ctk
import requests
from session import current_user
from PIL import Image, ImageTk
from model.config_model.config import NOTIFY_ICON, PROFILE_ICON
from model.config_model.config import API_URL

def iniciar_gui_inicio():
    inicio_app = ctk.CTk()
    inicio_app.title("Ecoscore - Inicio")
    inicio_app.geometry("1093x626")
    inicio_app.resizable(False, False)
    inicio_app.config(bg="#FFFAFA")
    ctk.set_appearance_mode("light")

    def preencher_dados_inicio():
        response = requests.get(
            f"{API_URL}/company/score/{current_user.cod_empresa}"
        )

        if response.status_code == 200:
            data = response.json()

            maior_score_btn.configure(text=f'Score Total\n do Mês: {data['score_mensal']}', wraplength=224,)

    frameEsq = ctk.CTkFrame(
        inicio_app,
        width=113,
        height=626,
        corner_radius=0,
    )
    frameEsq.pack(side="left")
    frameEsq.pack_propagate(False)

    canvasEsq = ctk.CTkCanvas(
        frameEsq,
        highlightthickness=0,
        bg='#FFFAFA'
    )
    canvasEsq.pack(fill='both', expand=True)

    def on_notify_click(event=None):
        print("Direciona para as notificações")

    try:
        pil_notify_icon = Image.open(NOTIFY_ICON).resize((34, 50))
        notify_icon = ImageTk.PhotoImage(pil_notify_icon)
        canvasEsq.notify_icon = notify_icon

        notify_btn = canvasEsq.create_image(124/2, 83, image=notify_icon)
        canvasEsq.tag_bind(notify_btn, "<Button-1>", on_notify_click)
    except FileNotFoundError:
        print(f"ERRO CRÍTICO: Arquivo de imagem não encontrado em: {NOTIFY_ICON}")
    except Exception as e:
        print(f"ERRO CRÍTICO ao carregar a imagem de notificação: {e}")

    frameDir = ctk.CTkFrame(
        inicio_app,
        width=113,
        height=626,
        corner_radius=0,
    )
    frameDir.pack(side="right")
    frameDir.pack_propagate(False)

    canvasDir = ctk.CTkCanvas(
        frameDir,
        highlightthickness=0,
        bg='#FFFAFA'
    )
    canvasDir.pack(fill='both', expand=True)

    def on_profile_click(event=None):
        from model.model_loading.model_loading import show_loading_screen
        from model.model_perfil.model_perfil import iniciar_gui_perfil
        #print("Direciona para o profile da empresa")
        inicio_app.destroy()
        show_loading_screen(iniciar_gui_perfil)
    
    try:
        pil_profile_icon = Image.open(PROFILE_ICON).resize((50, 50))
        profile_icon = ImageTk.PhotoImage(pil_profile_icon)
        canvasDir.profile_icon = profile_icon

        profile_btn = canvasDir.create_image(124/2, 83, image=profile_icon)
        canvasDir.tag_bind(profile_btn, "<Button-1>", on_profile_click)
    except FileNotFoundError:
        print(f"ERRO CRÍTICO: Arquivo de imagem não encontrado em: {NOTIFY_ICON}")
    except Exception as e:
        print(f"ERRO CRÍTICO ao carregar a imagem de notificação: {e}")
    
    frame = ctk.CTkFrame(
        inicio_app,
        width=850,
        height=513,
        corner_radius=0,
        fg_color='transparent'
    )
    frame.pack()
    frame.pack_propagate(False)

    canvas = ctk.CTkCanvas(
        frame,
        highlightthickness=0,
        bg="#FFFAFA"
    )
    canvas.pack(fill='both', expand=True)

    perguntas_btn = ctk.CTkButton(
        canvas,
        width=280,
        height=253,
        corner_radius=30,
        border_spacing=5,
        fg_color="#4E5D4D",
        text="PERGUNTAS",
        font=("Inter", 24, "bold"),
        text_color="#FFFAFA",
        #command=
    )

    canvas.create_window(
        138,
        149,
        anchor='center',
        window=perguntas_btn
    )

    maior_score_btn = ctk.CTkButton(
        canvas,
        width=280,
        height=253,
        corner_radius=30,
        border_spacing=5,
        fg_color="#4E5D4D",
        text="SEU MAIOR SCORE",
        font=("Inter", 24, "bold"),
        text_color="#FFFAFA",
        #command=
    )

    canvas.create_window(
        423,
        149,
        anchor='center',
        window=maior_score_btn
    )

    grafico_btn = ctk.CTkButton(
        canvas,
        width=280,
        height=253,
        corner_radius=30,
        border_spacing=5,
        fg_color="#4E5D4D",
        text="MEU GRÁFICO",
        font=("Inter", 24, "bold"),
        text_color="#FFFAFA",
        #command=
    )

    canvas.create_window(
        708,
        149,
        anchor='center',
        window=grafico_btn
    )

    inicio_app.after(50, preencher_dados_inicio)
    inicio_app.mainloop()
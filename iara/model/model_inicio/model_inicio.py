import customtkinter as ctk
from PIL import Image, ImageTk
from model.config_model.config import NOTIFY_ICON, PROFILE_ICON

def iniciar_gui_inicio():
    inicio_app = ctk.CTk()
    inicio_app.title("Ecoscore - Inicio")
    inicio_app.geometry("1093x626")
    inicio_app.resizable(False, False)
    inicio_app.config(bg="#FFFAFA")
    ctk.set_appearance_mode("light")

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

    inicio_app.mainloop()
import customtkinter as ctk
from PIL import Image

LOGO_PATH = r"C:\Users\ihorr\Desktop\Graduacao\1. CienciaComputacao\1. Semestre\1. APS\iara\model\src\logo.png"

def show_loading_screen(next_function):
    loading_app = ctk.CTk()
    loading_app.title("EcoScore - Iniciando")
    loading_app.geometry("400x300")
    loading_app.resizable(False, False)
    loading_app.config(bg="#1a1a1a")
    loading_app.eval('tk::PlaceWindow . center')

    # === LOGO ===
    try:
        logo = ctk.CTkImage(
            light_image=Image.open(LOGO_PATH),
            dark_image=Image.open(LOGO_PATH),
            size=(120, 120)
        )
        logo_label = ctk.CTkLabel(loading_app, image=logo, text="")
        logo_label.pack(pady=20)
    except Exception as e:
        print(f"[AVISO] Não foi possível carregar o logo: {e}")

    # === TEXTO ===
    label = ctk.CTkLabel(loading_app, text="Carregando... 0%", font=("Segoe UI", 18, "bold"), text_color="white")
    label.pack(pady=10)

    # === BARRA DE CARREGAMENTO ===
    progress = ctk.CTkProgressBar(loading_app, width=250, height=20, progress_color="#00b050", fg_color="#333")
    progress.pack(pady=15)
    progress.set(0)

    # === Atualização da barra ===
    def atualizar_barra(i=0):
        if i <= 100:
            progress.set(i / 100)
            label.configure(text=f"Carregando... {i}%")
            i += 1
            loading_app.after(20, atualizar_barra, i)
        else:
            loading_app.destroy()
            next_function()  # chama a próxima tela (login)

    atualizar_barra()
    loading_app.mainloop()

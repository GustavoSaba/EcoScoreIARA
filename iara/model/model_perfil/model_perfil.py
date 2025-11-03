import customtkinter as ctk
from PIL import Image, ImageTk
from model.config_model.config import HOME_ICON, NOTIFY_ICON, GRAPH_ICON
from api.config_api.config import EXCEL_PATH

def iniciar_gui_perfil():
    perfil_app = ctk.CTk()
    perfil_app.title("EcoScore - Perfil")
    perfil_app.geometry("1093x626")
    perfil_app.resizable(False, False)
    perfil_app.config(bg="#FFFAFA")

    frame = ctk.CTkFrame(
        perfil_app,
        width=124,
        height=626,
        corner_radius=0,
        fg_color="transparent"
        )
    frame.pack(side="left")
    frame.pack_propagate(False)

    canvas = ctk.CTkCanvas(
        frame,
        width=124,
        height=626,
        highlightthickness=0,
        bg="#FFFAFA"
    )
    canvas.pack(fill='both', expand=True)

    def on_home_click(event=None):
        print("Direciona para tela Inicial")

    def on_notify_click(event=None):
        print("Direciona para as notificações")

    def on_graph_click(event=None):
        print("Direciona para os gráficos")

    pil_home_icon = Image.open(HOME_ICON).resize((51, 50))
    home_icon = ImageTk.PhotoImage(pil_home_icon)

    home_btn = canvas.create_image(124/2, 82, image=home_icon)
    canvas.tag_bind(home_btn, "<Button-1>", on_home_click)

    pil_notify_icon = Image.open(NOTIFY_ICON).resize((34, 50))
    notify_icon = ImageTk.PhotoImage(pil_notify_icon)

    notify_btn = canvas.create_image(124/2, 199, image=notify_icon)
    canvas.tag_bind(notify_btn, "<Button-1>", on_notify_click)

    pil_graph_icon = Image.open(GRAPH_ICON).resize((34, 50))
    graph_icon = ImageTk.PhotoImage(pil_graph_icon)

    graph_btn = canvas.create_image(124/2, 317, image=graph_icon)
    canvas.tag_bind(graph_btn, "<Button-1>", on_graph_click)

    frame_principal = ctk.CTkFrame(
        perfil_app,
        width=845, 
        height=626, 
        corner_radius=0,
        fg_color="transparent"
    )
    frame_principal.pack(side="left")
    frame_principal.pack_propagate(False)

    '''frame_principal_cima = ctk.CTkFrame(
        frame_principal,
        width=579, 
        height=224, 
        corner_radius=0,
        fg_color="#E0E0D4",
        bg_color="#FFFAFA"
    )
    frame_principal_cima.place(relx = 0.5, rely = 0.5, anchor='n')'''

    canvas_principal = ctk.CTkCanvas(
        frame_principal,
        width=845,
        height=626,
        highlightthickness=0,
        bg="#FFFAFA"
    )
    canvas_principal.pack(fill='both', expand=True)

    bloco_info = ctk.CTkFrame(
        canvas_principal,
        width= 578,
        height= 224,
        fg_color="#E0E0D4",
        corner_radius=10,
    )
    
    canvas_principal.create_window(
        845/2,
        167,
        window=bloco_info
    )

    canvas_principal.create_text(
        845/2,
        172,
        text="",
        fill="#4E5D4D"
    )



    perfil_app.mainloop()
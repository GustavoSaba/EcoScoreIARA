import customtkinter as ctk
import pywinstyles as pwstyles
#import tkinter as tk
from model.config_model.config import BG_CADASTRO, LOGO_PATH
from PIL import Image

def iniciar_gui_cadastro():
    cadastro_app = ctk.CTk()
    cadastro_app.title("EcoScore - Cadastro")
    cadastro_app.geometry("1093x626")
    cadastro_app.resizable(False, False)
    ctk.set_appearance_mode("light")

    invis_color = "#1a1a1a"

    cadastro_app.configure(fg_color = invis_color)

    frame = ctk.CTkFrame(
        cadastro_app, 
        width=367, 
        height=626, 
        corner_radius=0,
        fg_color=invis_color
        )
    frame.pack(side="left")
    frame.pack_propagate(False)


    # Imagem de Fundo
    bg_cadastro = ctk.CTkImage(Image.open(BG_CADASTRO), size=(368,626))
    bg_label = ctk.CTkLabel(
        frame, 
        image=bg_cadastro, 
        text="",
        fg_color=invis_color
        )
    #bg_label.grid(row=0, column=0, pady=0, padx=0)
    bg_label.place(relx=0.5, rely=0.5, anchor='center')


    # Logo
    logo = ctk.CTkImage(Image.open(LOGO_PATH).convert("RGBA"), size=(94,103))
    logo_label = ctk.CTkLabel(
        bg_label,  
        image=logo, 
        text="",
        bg_color=invis_color
        )
    #logo_label.pack(pady=20)
    #pwstyles.set_opacity(logo_label, 1, "#000001")
    #logo_label.grid(row=0, column=0, pady=248, padx=136)
    logo_label.place(relx=0.5, rely=0.3968, anchor='n')
    
    sustentavel = ctk.CTkLabel(
        bg_label,
        text = "Seja sustentável!",
        font=("Poppins", 14),
        width=120,
        height=15,
        text_color="#FFFAFA",
        bg_color=invis_color
    )
    sustentavel.place(relx=0.5, rely=0.5808, anchor='n')

    #cadastro_app.wm_attributes("-transparentcolor", "#333333")
    #pwstyles.set_opacity(logo_label, color="#FFFAFA")
    cadastro_app.wm_attributes("-transparentcolor", invis_color)

    cadastro_app.mainloop()
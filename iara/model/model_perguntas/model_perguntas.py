import customtkinter as ctk
import requests
from session import current_user
from PIL import Image, ImageTk
from model.config_model.config import API_URL

def iniciar_gui_perguntas():
    perguntas_app = ctk.CTk()
    perguntas_app.title("Ecoscore - Perguntas")
    perguntas_app.geometry("1093x626")
    perguntas_app.resizable(False, False)
    perguntas_app.config(bg="#FFFAFA")
    ctk.set_appearance_mode("light")

    
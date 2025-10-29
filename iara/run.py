import threading
import time
import uvicorn
import requests
from model.model_login.model_login import iniciar_gui

API_URL = "http://127.0.0.1:8000"

def run_api():
    print("\033[93m[API] Iniciando servidor FastAPI...\033[0m")
    uvicorn.run("api.main:app", host="127.0.0.1", port=8000, reload=False)

def verificar_api():
    for tentativa in range(10):
        try:
            response = requests.get(f"{API_URL}/docs") 
            if response.status_code == 200:
                print("\033[92m[API] Servidor FastAPI está online!\033[0m")
                return True
        except requests.exceptions.ConnectionError:
            pass
        print(f"[API] Tentativa {tentativa+1}/10: aguardando servidor subir...")
        time.sleep(1)
    print("\033[91m[ERRO] API não respondeu após 10 tentativas.\033[0m")
    return False

if __name__ == "__main__":
    print("\033[96m============================================\033[0m")
    print("\033[96m🚀 Iniciando sistema EcoScore (API + Interface)\033[0m")
    print("\033[96m============================================\033[0m")

    api_thread = threading.Thread(target=run_api, daemon=True)
    api_thread.start()

    if verificar_api():
        print("\033[94m[GUI] Abrindo interface do EcoScore...\033[0m")
        iniciar_gui()
    else:
        print("\033[91m[ERRO] Não foi possível iniciar a interface — API fora do ar.\033[0m")

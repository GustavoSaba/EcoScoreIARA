from fastapi import HTTPException
import pandas as pd
from config import EXCEL_PATH


def autenticar_empresa(empresa_id: int):
    df_login = pd.read_excel(EXCEL_PATH, sheet_name='login_empresa')
    login = df_login[
        (df_login['cod_empresa_FK'] == empresa_id) &
        (df_login['login_auth'] == 1)
    ]
    if login.empty:
        raise HTTPException(status_code=404, detail="Empresa não autenticada!")
    return True

def autenticar_usuario(user_id: int):
    df_login = pd.read_excel(EXCEL_PATH, sheet_name='login_user')
    login = df_login[
        (df_login['cod_user_FK'] == user_id) &
        (df_login['login_auth'] == 1)
    ]
    if login.empty:
        raise HTTPException(status_code=404, detail="Usuario não autenticado!")
    return True

def user_amdin(auth: bool, user_id: int):
    df_login = pd.read_excel(EXCEL_PATH, sheet_name='user')
    login = df_login[
        (df_login['cod_user'] == user_id) &
        (df_login['user_type'] == 1)
    ]
    if login.empty:
        raise HTTPException(status_code=404, detail="Não é administrador!")
    return True
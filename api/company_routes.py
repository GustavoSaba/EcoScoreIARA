import pandas as pd
from fastapi import APIRouter, HTTPException
from config import EXCEL_PATH
from __modules import autenticar_empresa, autenticar_usuario, user_admin
from __classes import Empresa, EmpresaUpdate

company_router = APIRouter(prefix="/company", tags=["company"])

@company_router.get("/all")
async def get_all(user_id: int):
    df_database = pd.read_excel(EXCEL_PATH, sheet_name=None)
    df_empresa = df_database["empresa"]
    auth = autenticar_usuario(user_id)

    if auth:
        admin = user_admin(auth, user_id)
        if admin:
            companies = df_empresa.to_dict(orient="records")
    return companies

@company_router.get("/{cod_empresa}")
async def get_company(cod_empresa: int):

    df_database = pd.read_excel(EXCEL_PATH, sheet_name=None)
    df_empresa = df_database["empresa"]
    auth = autenticar_empresa(cod_empresa)

    if auth:
        empresa = df_empresa[df_empresa['cod_empresa'] == cod_empresa]
        empresa_teste = empresa.to_dict(orient="records")
    return empresa_teste


@company_router.put("/registrar")
async def put_company(nova_empresa: Empresa):
    df_database = pd.read_excel(EXCEL_PATH, sheet_name=None)
    df_empresa = df_database["empresa"]

    if df_empresa.empty:
        novo_cod = 1
    else:
        novo_cod = int(df_empresa['cod_empresa'].max() + 1)

    nova_linha = {
        "cod_empresa": novo_cod,
        **nova_empresa.dict()
    }
    
    df_empresa = pd.concat([df_empresa, pd.DataFrame([nova_linha])], ignore_index=True)
    with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
        df_empresa.to_excel(writer, sheet_name="empresa", index=False)
        for sheet_name, df_sheet in df_database.items():
            if sheet_name != "empresa":
                df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)
    return {"mensagem": "Empresa cadastrada com sucesso!", "cod_empresa": novo_cod}


@company_router.patch("/{cod_empresa}")
async def atualizar_empresa(cod_empresa: int, dados: EmpresaUpdate):
    df_database = pd.read_excel(EXCEL_PATH, sheet_name=None)
    df_empresa = df_database["empresa"]
    auth = autenticar_empresa(cod_empresa)

    if auth: 
        if not df_empresa['cod_empresa'].eq(cod_empresa).any():
            raise HTTPException(status_code=404, detail="Empresa não encontrada")

        atualizacoes = dados.dict(exclude_unset=True)
        for coluna, valor in atualizacoes.items():
            df_empresa.loc[df_empresa['cod_empresa'] == cod_empresa, coluna] = valor

        with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df_empresa.to_excel(writer, sheet_name="empresa", index=False)
            for sheet_name, df_sheet in df_database.items():
                if sheet_name != "empresa":
                    df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)

        return {"mensagem": "Empresa atualizada com sucesso!", "cod_empresa": cod_empresa}


@company_router.delete("/{cod_empresa}")
async def deletar_empresa(cod_empresa: int):
    df_database = pd.read_excel(EXCEL_PATH, sheet_name=None)
    df_empresa = df_database["empresa"]
    df_login_empresa = df_database["login_empresa"]
    auth = autenticar_empresa(cod_empresa)

    if auth: 
        if not df_empresa['cod_empresa'].eq(cod_empresa).any():
            raise HTTPException(status_code=404, detail="Empresa não encontrada")
        
        df_empresa = df_empresa[df_empresa['cod_empresa'] != cod_empresa]
        df_login_empresa = df_login_empresa[df_login_empresa['cod_empresa_FK'] != cod_empresa]

        with pd.ExcelWriter(EXCEL_PATH, engine="openpyxl", mode="a", if_sheet_exists="replace") as writer:
            df_empresa.to_excel(writer, sheet_name="empresa", index=False)
            df_login_empresa.to_excel(writer, sheet_name="login_empresa", index=False)
            for sheet_name, df_sheet in df_database.items():
                if sheet_name not in ["empresa", "login_empresa"]:
                    df_sheet.to_excel(writer, sheet_name=sheet_name, index=False)

        return {"mensagem": "Empresa deletada com sucesso!", "cod_empresa": cod_empresa}

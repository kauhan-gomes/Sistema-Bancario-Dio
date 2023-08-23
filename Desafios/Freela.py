import xmltodict
import os
import json

def pegar_infos(nome_arquivo):
    print(f"Pegou as informações {arquivo}")
    with open(f'NFS/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dic_arquivo, indent=4))
        infos_nf = dic_arquivo['NFe']
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf['emit']['xNome']
        nome_cliente = infos_nf['dest']['xNome']
        endereco = infos_nf['dest']["enderDest"]
        peso = infos_nf["transp"]["vol"]["pesoB"]
        print(numero_nota, empresa_emissora, nome_cliente, endereco, peso)

lista_arquivos = os.listdir("NFS")

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    break
import os

def buscar_arquivos(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        print(f"Erro: A pasta {caminho_pasta} não foi encontrada.")
        return []
        
    arquivos_encontrados = []
    
    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.endswith(('.docx', '.pdf')):
            caminho_completo = os.path.join(nome_arquivo)
            arquivos_encontrados.append(caminho_completo)
            
    return arquivos_encontrados


dados = buscar_arquivos(r"C:\Users\Felipe\Desktop\Ecoa - PUC\Site Cifra\Cifras prontas")
print(dados)
import os
import shutil

# Caminho da pasta
pasta_alvo = input("Digite o caminho da pasta que você que organizar: ")

# Mapeamento
tipos_de_arquivos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'PDFs': ['.pdf'],
    'Textos': ['.txt', '.doc', '.docx'],
    'Planilhas': ['.xls', '.xlsx', '.csv'],
    'Outros': []
}

# Criar subpastas que não existem
for pasta in tipos_de_arquivos.keys():
    caminho_pasta = os.path.join(pasta_alvo, pasta)
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)

# Mover arquivos
for arquivo in os.listdir(pasta_alvo):
    caminho_arquivo = os.path.join(pasta_alvo, arquivo)
    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        movido = False
        for pasta, extensoes in tipos_de_arquivos.items():
            if extensao.lower() in extensoes:
                shutil.move(caminho_arquivo, os.path.join(pasta_alvo, pasta, arquivo))
                print(f"Movido: {arquivo} -> {pasta}/")
                movido = True
                break
        if not movido:
            shutil.move(caminho_arquivo, os.path.join(pasta_alvo, 'Outros', arquivo))
            print(f"Movido: {arquivo} -> Outros/")
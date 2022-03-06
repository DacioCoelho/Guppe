"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos.
Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários,
 e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar
 o seguinte arquivo, chamado "usuarios.txt":

"""

lista_de_dados = []

def transformar_megabytes(tamanho_bytes:str) -> float:
    return int(tamanho_bytes)/(2**10)**2

with open ('C:/Users/Dácio/PycharmProjects/guppe/usuarios.txt.py', 'r') as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        usuario = linha[:15]
        tamanho_disco = transformar_megabytes(linha[16:])
        lista_de_dados.append((usuario, tamanho_disco))

cabeçalho = """
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

"""

with open('C:/Users/Dácio/PycharmProjects/guppe/relatorio.txt.py', 'w') as arquivo:
    tamanho_total = sum(tamanho for _, tamanho in lista_de_dados)
    media = tamanho_total / len(lista_de_dados)
    arquivo.writelines(cabeçalho)

    for indice,dados in enumerate(lista_de_dados, start=1):
        usuario, tamanho_disco = dados
        arquivo.writelines(f'{indice:<4}{usuario:<10}{tamanho_disco:9.2f} MB         {(tamanho_disco/tamanho_total):8.2%}\n')

    base = f"""
Espaço total ocupado: {tamanho_total:.2f} MB
Espaço médio ocupado: {media:.2f} MB"""
    arquivo.writelines(base)
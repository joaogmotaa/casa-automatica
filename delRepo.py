import requests

GITHUB_USERNAME = 'joaogmotaa'
GITHUB_TOKEN = 'token'
REPOSITORIOS_PARA_MANTER = [
    'nome',
    'nome',
    'nome',
    'nome',
    'nome',
]
def listar_repositorios():
    url = 'https://api.github.com/user/repos?per_page=100'
    resposta = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if resposta.status_code == 200:
        return [repo['name'] for repo in resposta.json()]
    else:
        print(f'Erro ao listar repositórios: {resposta.status_code}')
        return []


def deletar_repositorio(repo):
    url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{repo}'
    resposta = requests.delete(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if resposta.status_code == 204:
        print(f' Repositório "{repo}" deletado com sucesso.')
    elif resposta.status_code == 404:
        print(f' Repositório "{repo}" não encontrado ou já foi deletado.')
    else:
        print(f' Erro ao deletar "{repo}": {resposta.status_code} - {resposta.text}')

todos_os_repos = listar_repositorios()
repos_para_deletar = [repo for repo in todos_os_repos if repo not in REPOSITORIOS_PARA_MANTER]

print(" Repositórios que serão deletados:")
for repo in repos_para_deletar:
    print(f'  - {repo}')

confirmar = input(" Tem certeza que deseja deletar esses repositórios? (s/n): ")
if confirmar.lower() == 's':
    for repo in repos_para_deletar:
        deletar_repositorio(repo)
else:
    print(" Cancelado.")

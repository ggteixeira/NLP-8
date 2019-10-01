# Importação de módulos
import requests
from bs4 import BeautifulSoup

#  Interação com o usuário
# url = input("Insira uma URL: ")
url = "https://manualdousuario.net/sobre/"
# Faz um requeset da URL e a salva numa variável
def get_page(url):
    return requests.get(url)

# Baixa todo o conteúdo da página referente à URL
def download_page(get_page):
    return get_page.content

# Parseia o HTML, dando uma 'prettifycada' nele.
def html_parse(download_page):
    return BeautifulSoup(download_page, "html.parser")

# Limpa parcialmente o conteúdo, salvando apenas texto presente na página
def html_clean(html_parse):
    return html_parse.findAll(text=True)

# Cria dinamicamente uma lista de tags a serem ignoradas
def set_blacklist(html_clean):
    blacklist = set([token.parent.name for token in html_clean])
    blacklist.remove('p')
    return blacklist

def deep_clean(set_blacklist, html_clean):
    output = str()
    for token in html_clean:
        if token.parent.name not in set_blacklist(html_clean):
            output += f"{token }\n"
    return output

print(deep_clean(set_blacklist, html_clean(html_parse(download_page(get_page(url))))))

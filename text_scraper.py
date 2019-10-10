# Importação de módulos
import os
import requests
import time
from bs4 import BeautifulSoup



# def get_default_url(default_url='http://hmpg.net/'):
#     input_url = input("Digite uma URL: ")
#     if len(input_url) == 0:
#         return default_url
#     else:
#         return input_url

# # Faz um request da URL e a salva numa variável
# def get_urls(url=None):
#     if url is None:
#         return requests.get(get_default_url())
#     else:
#         url = input()
#     return requests.get(url)

def get_urls():
    text_bulk = open('urls.txt', 'r', encoding="utf-8")
    urls_list = list()
    
    for url in text_bulk:
        urls_list.append(url)
    text_bulk.close()
    
    return urls_list

def get_pages(get_urls):
    responses_list = list()
    for url in get_urls:
        responses_list.append(requests.get(url))
    return responses_list

def download_pages(get_pages):
    for response in get_pages:
        text_file = open(f'corpora/corpus-{time.time()}.txt', 'r+')
        text_file.write(response.content)

def make_soup(download_pages):
    directory = os.fsdecode("corpora")
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            text_file = open(file, 'r+')
            print(text_file.read())

# Pegar a lista de responses e baixar seus contents.
# Decidir se vai fazer isso num só arquivo ou em vários -- ou numa variável.
# Usar o código que está na master pra verificar qual é o melhor approach.


# Baixa todo o conteúdo da página referente à URL
# def download_pages(get_urls):
#     downloaded_page = open(f'corpora/corpus_{time.time().txt}', 'w')
#     for url in get_urls:
#         downloaded_page.

    # return get_page.content


# Parseia o HTML, dando uma 'prettifycada' nele.
def html_parse(download_page):
    return BeautifulSoup(download_page, "html.parser")


# Limpa parcialmente o conteúdo, salvando apenas texto presente na página
def html_clean(html_parse):
    return html_parse.findAll(text=True)


# Cria dinamicamente uma lista de tags a serem ignoradas
def set_blacklist(html_clean):
    blacklist = set([token.parent.name for token in html_clean])
    blacklist.remove("p")
    return blacklist


# Printa todos os tokens, menos aqueles cujos pais estão na blacklist
def deep_clean(set_blacklist, html_clean):
    output = str()
    for token in html_clean:
        if token.parent.name not in set_blacklist(html_clean):
            output += f"{token }\n"
    return output

def write_into_file(deep_clean):
    text_file = open(f'corpora/corpus_{time.time()}.txt', 'w')
    for token in deep_clean:
        text_file.write(token)
    text_file.close()


# print(write_into_file(deep_clean(set_blacklist, html_clean(html_parse(download_page(get_urls()))))))
print(make_soup(download_pages(get_pages(get_urls()))))
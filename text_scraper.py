# Importação de módulos
import requests
from bs4 import BeautifulSoup

#  Interação com o usuário
url = input("Insira uma URL: ")

# Faz um requeset da URL e a salva numa variável
res = requests.get(url)

# Baixa todo o conteúdo da página referente à URL
html_page = res.content

# Parseia o HTML, dando uma 'prettifycada' nele.
soup = BeautifulSoup(html_page, "html.parser")

# Limpa parcialmente o conteúdo, salvando apenas texto presente na página
text = soup.findAll(text=True)

output = str()
blacklist = set([t.parent.name for t in text])
blacklist.remove('p')

for t in text:
    if t.parent.name not in blacklist:
        output += f"{t}\n"

print(output)

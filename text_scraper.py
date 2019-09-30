import requests

url = "https://manualdousuario.net/celular-pirata-nao-homologado-bloqueio/"
res = requests.get(url)
html_page = res.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, "html.parser")

text = soup.findAll(text=True)

# print(set([t.parent.name for t in text]))
output = " "
blacklist = [
    "link",
    "header",
    "ul",
    "a",
    "[document]",
    "form",
    "option",
    "time",
    "head",
    "html",
    "h3",
    "span",
    "b",
    "strong",
    "img",
    "em",
    "li",
    "h2",
    "select",
    "nav",
    "h1",
    "article",
    "body",
    "title",
    "label",
    "input",
    "div",
    "script",
    "i",
    "svg",
    "footer",
    "ol",
    "main",
    "meta",
]

for t in text:
    if t.parent.name not in blacklist:
        output += f"{t}"

print(output)

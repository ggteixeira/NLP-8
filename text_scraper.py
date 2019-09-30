import requests

url = "https://www.infowester.com/guiahdinic.php"
# url = input("URL: ")
res = requests.get(url)
html_page = res.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_page, "html.parser")

text = soup.findAll(text=True)

# set([t.parent.name for t in text])
output = " "
blacklist = set([t.parent.name for t in text])
blacklist.remove('p')
for t in text:
    if t.parent.name not in blacklist:
        output += f"{t}"

print(output)

from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

print(soup.title.string)

print(soup.prettify())

all_anchor_tags = soup.find_all(name='a')
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get_text())
    print(tag.get("href"))

company_url = soup.select_one(selector="p a")
print(company_url)
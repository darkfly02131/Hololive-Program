import requests
from bs4 import BeautifulSoup

search_term = input("Enter a Hololive member name or generation to search for: ")

url = f"https://hololive.hololivepro.com/en/talents?gp=hololive"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

talent_list = doc.find_all("div", {"class": "talent"})

talents_found = {}

for talent in talent_list:
    name_elem = talent.find("div", {"class": "talent-name"})
    name = name_elem.text.strip()
    
    gen_elem = talent.find("div", {"class": "talent-generation"})
    gen = gen_elem.text.strip()
    
    link_elem = talent.find("a", {"class": "talent-link"})
    link = link_elem.get("href")
    
    if search_term.lower() in name.lower() or search_term.lower() in gen.lower():
        talents_found[name] = {"generation": gen, "link": link}

sorted_talents = sorted(talents_found.items(), key=lambda x: x[1]['generation'])

for talent in sorted_talents:
    print(talent[0])
    print(talent[1]['generation'])
    print(talent[1]['link'])
    print("-------------------------------")

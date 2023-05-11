import requests as ses
from bs4 import BeautifulSoup

 
# Ask for the Hololive member's name or generation
search_term = input("What Hololive member or generation do you want to search for? ")

#Q:buddy c what's the syntax for the request_html library?
#Q: thanks buddy c
#A
# Set the search URL
url = f"https://hololive.hololivepro.com/en/talents/{search_term}"
reponse = ses.get(url)
print(reponse)
# Retrieve the search page and parse it using BeautifulSoup
page = ses.get(url).text
doc = BeautifulSoup(page, "html.parser")
talent_links = []
# Find all search results that match the search term
talent_list = doc.find_all("ul", {"class": "talent-list clearfix"})
 #Find the total number of search results
#pages = int(str(talent_list).split("/")[-2].split(">")[-1][:-1])

# Calculate the number of pages based on the total number of search results (10 search results per page)

# Dictionary to store the search results
members_found = {}
# print(page)

# Loop through all search results
# for item in items:
    
#     # Extract the member's name and generation from the search result
#     name = item.find("p", {"class": "talents-name"}).text.strip()
#     generation = item.find("p", {"class": "talents-generation"}).text.strip()
    
#     # Extract the member's website link from the search result
#     link = item.find("a", {"class": "talents-link"})['href']
    
#     # Store the member's information in the dictionary
#     members_found[name] = {"generation": generation, "link": link}

# # Sort the search results by the member's generation
# sorted_members = sorted(members_found.items(), key=lambda x: x[1]['generation'])

# # Print the search results
# for member in sorted_members:
#     print(f"{member[0]} [{member[1]['generation']}]")
#     print(member[1]['link'])
#     print("-------------------------------")

for page in range(1, + 1):
    
    url = f"https://hololive.hololivepro.com/en/talents?gp=hololive&page={page}"
    page = ses.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    talents = doc.find_all("ul", {"class": "talent-list clearfix"})
items_found = {}
for talent in members_found:
    try:
        pagef = ses.urlopen(talent)
    except ses.HTTPError:
        continue
    url = f"https://hololive.hololivepro.com{search_term}"
    page = ses.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    

    talent_name = doc.find("div", {"class": "talent-list clearfix"}).text.strip()
    print(talent_name)
    talent_generation = doc.find("ul", {"class": "clearfix"}).text.strip()


    items_found[talent_name] = {"generation": talent_generation}
# print(items_found)

sorted_items = sorted(members_found.items(), key=lambda x: x[1]['generation'])

for item in sorted_items:
    print(item[0])
    print(item[1]['generation'])
    print(item[0] + item[1]['generation'])
    print("-------------------------------")


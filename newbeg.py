import requests
from bs4 import BeautifulSoup

# Ask for the Hololive member's name or generation
search_term = input("What Hololive member or generation do you want to search for? ")

# Set the search URL
url = f"https://hololive.hololivepro.com/en/talents?gp=hololive&search={search_term}"

# Retrieve the search page and parse it using BeautifulSoup
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

# Find all search results that match the search term
items = doc.find_all("div", {"class": "talent"})
 #Find the total number of search results
total_results = int(doc.find("p", {"class": "talents-count"}).text.strip().split()[0])

# Calculate the number of pages based on the total number of search results (10 search results per page)
pages = (total_results // 10) + (1 if total_results % 10 != 0 else 0)

# Dictionary to store the search results
members_found = {}

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

for page in range(1, pages + 1):
    url = f"https://hololive.hololivepro.com/en/talents?gp=hololive&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    talents = doc.find_all("div", {"class": "talent-item"})

    for talent in talents:
        name = talent.find("h4").text.strip()
        generation = talent.find("h5").text.strip()
        link = "https://www.youtube.com" + talent.find("a", href=True)["href"]
        
        if search_term.lower() in name.lower():
            members_found[name] = {"generation": generation, "link": link}

sorted_items = sorted(members_found.items(), key=lambda x: x[1]['generation'])

for item in sorted_items:
    print(item[0])
    print(item[1]['generation'])
    print(item[1]['link'])
    print("-------------------------------")
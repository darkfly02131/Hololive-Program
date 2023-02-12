import requests
from bs4 import BeautifulSoup


url = "https://hololive.hololivepro.com/en/talents"


# Send a GET request to the URL

response = requests.get(url)


# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")


#Find talent elements
talent_data = soup.find_all("div", class_="talent-data")



# Define an empty dictionary to store the talent data
member_dict = {}

for member_data in talent_data:
    #extract the name of the talent and generation data
    name = member_data.find("h4").text.strip()
    generation = member_data.find("p").text.strip()


#extract the youtube link
    youtube_link = member_data.find("a", href=True)["href"]
    #Create a dictionary for the member and store the data
    member_dict[name] + {"Name": name, "Generation": generation, "Youtube": youtube_link}

#print the member data for each member in the dictionary
name = input("Enter the name of the member to search for: ")

member = member_dict.get(name)
print(member_dict)
if member:
    print(f"Name:, {member['Name']}")
    print(f"Generation:, {member['Generation']}")
    print(f"Youtube:, {member['Youtube_Link']}")
else:
    print(f"{name} is not a valid member name")




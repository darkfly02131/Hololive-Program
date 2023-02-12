#Importing the required modules
import requests
from bs4 import BeautifulSoup

#Defining the URL to scrap
url = "https://hololive.hololivepro.com/en/talents"

#Send a GET request to the URL
response = requests.get(url)

#Parse the HTML content using Beautiful Soup 
soup = BeautifulSoup(response.content, "html.parser")

#Find the HTML elemetns that contains the member 
talent_elements = soup.find_all("div", class_="talent")
generation_elements = soup.find_all("div", class_="generation")

#Define Empty list to store member and gen info
talent_data = {}


#iterate over the member and gen elements  and extract text content
for talent in talent_elements:
    #Extract the name of the talent
    name= talent.find("h2").text.strip()

    #Extract the image URL of the talent
    image_url = talent.find("img")["src"]

    #Extract the description of the talent
    description = talent.find("p").text.strip()
    #Extract the social media links of the talent
    links = {}
    for link in talent.find_all("a"):
        platform= link.text.strip()
        url=link["href"]
        links[platform]=url

    #Create a dictionary to store the talent data and add it to the talent_data dictionary
    talent_data[name] = {
        "image_url": image_url,
        "description": description,
        "links": links

    }
    #Ask the user to input a talent name to search for
    talent_name = input("Enter the name of the talent to search for: ")

    #Look up the talent in the talent_data dictionary
    talent_info = talent_data.get(talent_name)

    #check if the talent was found and print their information
    if talent_info:
        print("Name:", talent_name)
        print("Image URL:", talent_info["image_url"])
        print("Description:", talent_info["description"])
        print("Links:")
        for platform, url in talent_info["links"].items():
            print(f"{platform}: {url}")
    else:
        print("Talent not found")




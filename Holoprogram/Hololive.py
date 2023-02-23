import requests
from io import BytesIO
from bs4 import BeautifulSoup
import tkinter as tk
from PIL import Image, ImageTk

#retrieve hololive english talents page

class Character:
    def __init__(self, name, generation, youtube_link, image_url):
        self.name = name
        self.generation = generation
        self.youtube_link = youtube_link
        self.image_url = image_url

    def __str__(self):
        return f"{self.name} (Generation {self.generation}): {self.youtube_link}"
root= tk.Tk()


def create_talent_dict():
    url = "https://hololive.hololivepro.com/en/talents"
    response= requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    talents = soup.find_all("div", {"class": "talent"})
    talent_dict = {}
    for talent_div in soup.find_all("div", {"class": "talent"}):
        name = talent_div.find("h4").text
        generation = talent_div.find("h5").text
        youtube_link = talent_div.find("a", {"class": "youtube-link"})["href"]
        image_url = talent_div.find("img")["src"]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        talent_dict[name] = {"generation": generation, "youtube_link": youtube_link, "image_url": image_url}
   
    return talent_dict, 




#create a tkinter window and display the talent information


def display_talent(name):
    # get the information for the given talent name from the talent_dict
    # talent_info = talent_dict.get(name)
    print(type(name))
    selected_character = talent_dict.get(name)
    if selected_character is None:
        info_label.config(text="No information found for {name}")
        image_label.config(image=None)
        return
    info_text = f"Name: {selected_character.name}\nGeneration: {selected_character.generation}\nYoutube Link: {selected_character.youtube_link}"
    info_label.config(text=info_text)
    image_url = selected_character.image_url
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo


talent_dict = create_talent_dict()

characterName = tk.StringVar(root)
characterName.set("Select a character")



characterMenu = tk.OptionMenu(root, characterName, *talent_dict, command=lambda name: display_talent(name))
characterMenu.pack()

# name_label = tk.label(root,text= f"Name: {.name}")f

info_label = tk.Label(root)
info_label.pack()

image_label = tk.Label(root)
image_label.pack()

button= tk.Button(root, text="Display character info", command=display_talent)
button.pack()

root.mainloop()






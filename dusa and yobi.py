import matplotlib.pyplot as plt
import numpy as np
import requests
import tkinter as tk

api_key = '7e424946a7314ef515c547339e797d8e'


name = tk.Label( text="Enter city in Canada")
name.pack()
page = tk.Entry()
page.pack()


url = f'http://api.openweathermap.org/data/2.5/weather?q={name}&appid={api_key}'

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

response = requests.get(url)

data = response.json()
#this helps so that  If the city is found, the code extracts the temperature information and plot it.
if data['cod'] != '404':
    kelvin_temp = data['main']['temp']
    celsius, fahrenheit = kelvin_to_celsius_fahrenheit(kelvin_temp)

    print(f'Temperature: {celsius} °C')
    print(f'Temperature: {fahrenheit} °F')

    xpoints = np.array([1, 8])
    ypoints = np.array([celsius, fahrenheit])

    plt.plot(xpoints, ypoints, marker='o')
    plt.xlabel('Temperature')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig("squares.png")
    plt.show()

else:
    print('City not found.')
# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
win = tk.Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)



# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("squares.png"))



import tkinter as tk
import requests

def NewsFromBBC():
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = "https://newsapi.org/v1/articles"

    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    # update the text box with the news
    for i in range(len(results)):
        text_box.insert(tk.END, f"{i + 1}. {results[i]}\n")

# Driver Code
if __name__ == '__main__':
    # create the tkinter window


    # create the text box
    text_box = tk.Text(win, wrap=tk.WORD)
    text_box.pack(fill=tk.BOTH, expand=True)

    # function call
    NewsFromBBC()


    # start the tkinter event loop
    win.mainloop()
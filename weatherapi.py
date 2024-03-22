import tkinter as tk
import requests
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

api_key = '7e424946a7314ef515c547339e797d8e'

# Main window
win = tk.Tk()
win.title("Weather News")

# News frame
news_frame = tk.LabelFrame(win, text="News")
news_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Text box for news
text_box = tk.Text(news_frame, wrap=tk.WORD)
text_box.grid(row=0, column=0, sticky="nsew")

# Graph frame
graph_frame = tk.LabelFrame(win, text="Temperature Graph")
graph_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Function to fetch news


def newsFromBBC():
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
    text_box = tk.Text(news_frame, wrap=tk.WORD)
    text_box.grid(row=0, column=0, sticky="nsew")


    # function call
    newsFromBBC()

# Function to fetch weather
def fetch_weather():
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        kelvin_temp = data["main"]["temp"]
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(kelvin_temp)
        xpoints = np.array([1, 8])
        ypoints = np.array([celsius, fahrenheit])
        fig, ax = plt.subplots()
        ax.plot(xpoints, ypoints, marker='o')
        ax.set_xlabel("Temperature")
        ax.set_ylabel("Value")
        ax.set_title("Temperature Conversion")
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10)
    else:
        print("City not found.")

# Conversion function
def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

# City entry and buttons
city_label = tk.Label(win, text="Enter City:")
city_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
city_entry = tk.Entry(win)
city_entry.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
fetch_weather_button = tk.Button(win, text="Fetch Weather", command=fetch_weather)
fetch_weather_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


win.mainloop()

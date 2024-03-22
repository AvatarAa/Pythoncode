import tkinter as tk
import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image

api_key = '7e424946a7314ef515c547339e797d8e'  # Replace with your actual API key

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9 / 5) + 32
    return celsius, fahrenheit

def get_weather_data():
    """Retrieves weather data from API and creates plot."""
    city_name = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['cod'] != '404':
        kelvin_temp = data['main']['temp']
        celsius, fahrenheit = kelvin_to_celsius_fahrenheit(kelvin_temp)

        xpoints = np.array([1, 8])
        ypoints = np.array([celsius, fahrenheit])

        plt.figure(figsize=(5, 3))  # Adjust figure size if needed
        plt.plot(xpoints, ypoints, marker='o')
        plt.xlabel('Temperature')
        plt.ylabel('Value')
        plt.legend(['Celsius', 'Fahrenheit'])
        plt.savefig("squares.png")

        weather_image.config(image=img)
    else:
        print('City not found.')

def get_news_data():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = "https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    articles = open_bbc_page["articles"]

    results = []
    for article in articles:
        results.append(article["title"])

    news_text_box.delete("1.0", tk.END)
    for i, title in enumerate(results):
        news_text_box.insert(tk.END, f"{i + 1}. {title}\n")

# Create the main window
window = tk.Tk()
window.title("Weather and News")

# Create widgets for weather
city_label = tk.Label(window, text="Enter city in Canada:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()
get_weather_button = tk.Button(window, text="Get Weather", command=get_weather_data)
get_weather_button.pack()

weather_frame = tk.Frame(window, width=500, height=300)
weather_frame.pack()
weather_frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open("squares.png"))  # Load initial image
weather_image = tk.Label(weather_frame, image=img)
weather_image.pack()

# Create widgets for news
news_label = tk.Label(window, text="Top BBC News:")
news_label.pack()
news_text_box = tk.Text(window, wrap=tk.WORD)
news_text_box.pack(fill=tk.BOTH, expand=True)
get_news_button = tk.Button(window, text="Get News", command=get_news_data)
window.mainloop()
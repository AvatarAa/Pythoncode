import tkinter as tk
import requests
#the function
def on_click():
    book = page.get()
    chapter = admin.get()
    verse = reverse.get()
    url = "https://bible-api.com/" + book + "+" + chapter + ":" + verse
    response = requests.get(url)
    parsed_data = response.json()
    verses = parsed_data["verses"]
#this deletes the other scripture that has been printed
    text_box.delete(1.0, tk.END)
#this for is to print the book,chapter and verse
    for verse in verses:
        verse_text = f"{book} {verse['chapter']}:{verse['verse']}\n{verse['text']}\n"
        text_box.insert(tk.END, verse_text, "verse")

window = tk.Tk()
greeting = tk.Label(text="BIBLE SCRIPTURE FINDER")
greeting.pack()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
#this is the button present on frame 3, defined such that on click it would print out the scriptures.
button = tk.Button(master=frame3, text="SEARCH", width=25, height=5, bg="blue", fg="yellow", command=on_click)
button.pack(pady=10)

name = tk.Label(frame1, text="Input Book")
name.pack()
page = tk.Entry(frame1, bg="red")
page.pack()
chapter = tk.Label(frame1, text="Input Chapter")
chapter.pack()
admin = tk.Entry(frame1, bg="red")
admin.pack()
verse = tk.Label(frame1, text="Input Verse")
verse.pack()
reverse = tk.Entry(frame1, bg="red")
reverse.pack()
#the wrap makes so the words start on another line when there is no space to prevent autonmosy
text_box = tk.Text(frame2, wrap=tk.WORD)
text_box.pack(fill=tk.BOTH, expand=True)

window.mainloop()
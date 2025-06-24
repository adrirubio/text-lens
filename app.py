# app.py
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random

quotes = [
    '"I think, therefore I am ." - René Descartes',
    '"To be or not to be." - William Shakespear',
    '"Knowledge is power." - Francis Bacon',
    '"Stay hungry, stay foolish." - Steve Jobs',
    '"Time is money." - Benjamin Franklin',
    '"Simplicity is the ultimate sophistication." - Leonardo da Vinci',
    '"Fortune favors the brave." - Virgil',
    '"Imagination is more important than knowledge." - Albert Einstein',
    '"Power tends to corrupt." - Lord Acton',
    '"The medium is the message." - Marshall McLuhan',
    '"Creativity is intelligence having fun." - Albert Einstein',
    '"Less is more." - Ludwig Mies van der Rohe',
    '"Good artists copy; great artists steal." - Pablo Picasso',
    '"Injustice anywhere is a threat." - Martin Luther King Jr.',
    '"Speak softly and carry a big stick." - Theodore Roosevelt',
    '"Hope is a good breakfast." - Francis Bacon',
    '"Facts are stubborn things." - John Adams'
]

def fade_in_label(label, text, delay=40):
    for i in range(len(text)):
        window.after(i * delay, lambda i=i: label.config(text=text[:i+1]))

# Main window setup
window = tk.Tk()
window.title("Text Lens")
window.geometry("900x700")
window.configure(bg="grey20")
window.resizable(False, False)

# Fonts
quote_font = tkFont.Font(family="Crimson Text", size=23, slant="italic")
author_font = tkFont.Font(family="Times", size=17, weight="bold")
title_font = tkFont.Font(family="Times", size=27, weight="bold")
text_font = tkFont.Font(family="Helvetica", size=14)

# One stretching column
window.grid_columnconfigure(0, weight=1)

quote_frame = tk.Frame(window, bg="RoyalBlue2")
quote_frame.grid(row=0, column=0, sticky="ew")
quote_frame.grid_columnconfigure(0, weight=1)

# Quote
random_quote = random.choice(quotes)

before_dash, dash, after_dash = random_quote.partition('-')
quote_text = before_dash
author = after_dash
author_text = f"- {author}"

row_quote = tk.Frame(quote_frame, bg="RoyalBlue2")
row_quote.grid(row=0, column=0, sticky="ew")
row_quote.grid_columnconfigure(0, weight=1)

# Quote label
quote = tk.Label(
    row_quote,
    text=quote_text,
    fg="white",
    bg="RoyalBlue2",
    font=quote_font,
    wraplength=840,
    justify="center"
)
quote.grid(row=0, column=0, sticky="n", pady=10)
fade_in_label(quote, quote_text)

# Author label
author = tk.Label(
    row_quote,
    text=author_text,
    fg="white",
    bg="RoyalBlue2",
    font=author_font
)
author.grid(row=1, column=0, sticky="n", padx=5, pady=(0, 15))
fade_in_label(author, author_text)

# Text input box
input_frame = tk.Frame(window, bg="grey20")
input_frame.grid(row=1, column=0, sticky="new", padx=20, pady=(0, 20))
input_frame.grid_columnconfigure(0, weight=1)
input_frame.grid_rowconfigure(1, weight=1)

input_lbl = tk.Label(
    input_frame,
    text="📝 Paste your text here for analysis:",
    fg="white",
    bg="grey20",
    font=text_font
)
input_lbl.grid(row=0, column=0, columnspan=2, sticky="n", pady=15)

input_box = tk.Text(
    input_frame,
    font=text_font,
    wrap="word",
    bd=7,
    relief="groove",
    bg="grey63",
    fg="black",
    height=15
)
input_box.grid(row=1, column=0, sticky="ew")

scroll = tk.Scrollbar(
    input_frame,
    orient="vertical",
    command=input_box.yview
)
scroll.grid(row=1, column=1, sticky="ns")

input_box.config(yscrollcommand=scroll.set)

window.mainloop()


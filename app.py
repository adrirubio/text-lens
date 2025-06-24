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

row0 = tk.Frame(window, bg="RoyalBlue2")
row0.grid(row=0, column=0, sticky="ew")
row0.grid_columnconfigure(0, weight=1)

# Quote
random_quote = random.choice(quotes)

before_dash, dash, after_dash = random_quote.partition('-')
quote_text = before_dash
author = after_dash

row_quote = tk.Frame(row0, bg="RoyalBlue2")
row_quote.grid(row=1, column=0, sticky="ew")
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

# Author label
author = tk.Label(
    row_quote,
    text=f"- {author}",
    fg="white",
    bg="RoyalBlue2",
    font=author_font
)
author.grid(row=1, column=0, sticky="n")

window.mainloop()

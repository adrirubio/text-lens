# app.py
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import random
import re, math
from collections import Counter

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

def on_analyze(input_box, response_box, wpm=200):
    text = input_box.get("1.0", "end-1c")

    tokens = re.findall(r"\b\w+\b", text.lower())
    words  = len(tokens)
    unique = len(set(tokens))
    ttr    = unique / words if words else 0
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    avg_len   = words / len(sentences) if sentences else 0
    m, s      = divmod(math.ceil(words / wpm * 60), 60)

    response_box.delete("1.0", "end")
    response_box.insert("end", f"Words: {words:,}    Sentences: {len(sentences)}\n")
    response_box.insert("end", f"Avg. sentence length: {avg_len:.1f} words\n")
    response_box.insert("end", f"Unique words: {unique:,} \n")
    response_box.insert("end", f"Est. reading time: {m} min {s:02d} sec\n")

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
button_font = tkFont.Font(family="Helvetica", size=12, weight="bold")

# One stretching column
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)

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
input_frame.grid(row=1, column=0, sticky="new", padx=20)
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

# Analyze button
analyze = tk.Button(
    input_frame,
    text="Analyze",
    bg="RoyalBlue2",
    fg="white",
    activebackground="RoyalBlue3",
    activeforeground="#2E2E2E",
    width=14,
    height=1,
    relief="raised",
    bd=7,
    cursor="hand2",
    font=button_font,
    command=lambda: on_analyze(input_box, results_box)
)
analyze.grid(row=2, column=0, pady=15)

# output frame
output_frame = tk.Frame(window, bg="RoyalBlue2")
output_frame.grid(row=2, column=0, sticky="nsew")

# make the column expand
output_frame.grid_columnconfigure(0, weight=1)
output_frame.grid_rowconfigure(1,  weight=1)

result_lbl = tk.Label(
    output_frame,
    text="Basic insights on your text will appear here:",
    fg="white",
    bg="RoyalBlue2",
    font=text_font
)
result_lbl.grid(row=0, column=0, sticky="w", pady=10, padx=20)

results_box = tk.Text(
    output_frame,
    font=text_font,
    wrap="word",
    bd=7,
    relief="groove",
    bg="grey63",
    fg="black",
    width=45,
    height=10
)
results_box.grid(row=1, column=0, sticky="w", pady=(0, 5), padx=5)

window.mainloop()


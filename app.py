# app.py
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import re, math
from collections import Counter

graph_canvas = None

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

def show_input():
    global graph_canvas
    input_box.grid()
    scroll.grid()
    analyze.grid()

    # Restore label
    input_lbl.config(text="")
    input_lbl.config(text="📝 Paste your text here for analysis:")

    if graph_canvas:
        graph_canvas.get_tk_widget().grid_remove()

def show_top_words():
    global graph_canvas

    # Update label
    input_lbl.config(text="")
    input_lbl.config(text="📊 Top ten word frequencies in your text:")

    # Data
    text = input_box.get("1.0", "end-1c").lower()
    words = re.findall(r"\b\w+\b", text)
    if not words:
        return
    top = Counter(words).most_common(10) or [("none", 0)]
    labels, counts = zip(*reversed(top))

    input_box.grid_remove()
    scroll.grid_remove()
    analyze.grid_remove()

    # Build graph
    if graph_canvas is None:
        fig, ax = plt.subplots(figsize=(5, 3))
        graph_canvas = FigureCanvasTkAgg(fig, master=input_frame)
    else:
        fig = graph_canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)

    ax.barh(labels, counts, color="RoyalBlue")
    ax.set_xlabel("Frequency")
    ax.set_title("Top Words")
    fig.tight_layout()
    graph_canvas.draw()

    # Place graph
    graph_canvas.get_tk_widget().grid(
        row=1,
        column=0,
        columnspan=2,
        sticky="nsew",
        pady=30
    )

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

def on_right_click(event):
    w, h = 200, 100
    cur_x, cur_y = event.x_root, event.y_root
    x = cur_x
    y = cur_y + 20

    # Keep pop up on screen
    scr_w = window.winfo_screenwidth()
    scr_h = window.winfo_screenheight()
    x = max(0 , x)
    y = min(scr_h - h, y)

    click_win = tk.Toplevel(window)
    click_win.title("Right click")
    click_win.geometry(f"{w}x{h}+{x}+{y}")
    click_win.configure(bg="#2E2E2E")
    click_win.resizable(False, False)

    # Grid
    click_win.grid_columnconfigure(0, weight=1)
    click_win.grid_columnconfigure(1, weight=1)

    # Copy button
    copy_btn = tk.Button(
        click_win,
        text="Copy",
        font=button_font,
        bg="white",
        fg="black",
        activebackground="black",
        activeforeground="white",
        width=3,
        height=1,
        relief="raised",
        bd=7,
        command=lambda: on_copy(click_win)
    )
    copy_btn.grid(row=0, column=0, pady=30)

    # Paste button
    paste_btn = tk.Button(
        click_win,
        text="Paste",
        font=button_font,
        bg="white",
        fg="black",
        activebackground="black",
        activeforeground="white",
        width=3,
        height=1,
        relief="raised",
        bd=7,
        cursor="hand2",
        command=lambda: on_paste(click_win)
    )
    paste_btn.grid(row=0, column=1, pady=30)

def update_clear_state(event=None):
    text_present = bool(input_box.get("1.0", "end-1c").strip())

    chart_dd.config(state="normal" if text_present else "disabled")

def on_chart_select(choice):
    if choice != "Home":
        print("User selected:", choice)
    else:
        print("Back on Home")

    if choice == "Home":
        show_input()
    elif choice == "Top Words":
        show_top_words()

def on_clear(input_box, output_box):
    # Remove text inside of input box
    input_box.delete("1.0", tk.END)

    # Remove text inside of ouput_box
    output_box.delete("1.0", tk.END)

    # Disable chart_dd
    chart_dd.config(state="disabled")

def on_copy(window):
    text = input_box.get("1.0", "end-1c")
    window.clipboard_clear()
    window.clipboard_append(text)
    window.destroy()

def on_paste(window):
    clipboard = window.clipboard_get()
    input_box.insert("insert", clipboard)
    window.destroy()

def fade_in_label(label, text, delay=40):
    for i in range(len(text)):
        window.after(i * delay, lambda i=i: label.config(text=text[:i+1]))

def on_exit():
    plt.close("all")
    window.destroy()
    window.quit()

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
input_box.bind("<Button-3>", on_right_click)

scroll = tk.Scrollbar(
    input_frame,
    orient="vertical",
    command=input_box.yview
)
scroll.grid(row=1, column=1, sticky="ns")
input_box.config(yscrollcommand=scroll.set)
input_box.bind("<KeyRelease>", update_clear_state)
input_box.bind("<<Paste>>", update_clear_state)
input_box.bind("<<Cut>>", update_clear_state)

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

# Clear button
clear_btn = tk.Button(
    output_frame,
    text="Clear",
    bg="RoyalBlue2",
    fg="white",
    activebackground="RoyalBlue3",
    activeforeground="#2E2E2e",
    width=10,
    height=1,
    relief="raised",
    bd=7,
    cursor="hand2",
    font=button_font,
    command=lambda: on_clear(input_box, results_box)
)
clear_btn.grid(row=1, column=0, sticky="e", padx=220)

# Graph dropdown
chart_var = tk.StringVar(value="Home")

chart_dd = tk.OptionMenu(
    output_frame,
    chart_var,
    "Home",
    "Top Words",
    "Sentences",
    "Punctuation",
    command=on_chart_select
)
chart_dd.config(
    bg="RoyalBlue2",
    fg="white",
    activebackground="RoyalBlue3",
    activeforeground="#2E2E2E",
    font=button_font,
    width=10,
    relief="raised",
    bd=7
)
chart_dd["menu"].config(
    bg="RoyalBlue2",
    fg="white",
    activebackground="RoyalBlue3",
    activeforeground="white",
    font=button_font
)
chart_dd.grid(row=1, column=0, sticky="e", padx=30)
chart_dd.config(state="disabled")

window.protocol("WM_DELETE_WINDOW", on_exit)
window.mainloop()


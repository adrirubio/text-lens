# app.py
import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk
from PIL import Image, ImageTk

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
quotes_font = tkFont.Font(family="Crimson Text", size=16, slant="italic")
title_font = tkFont.Font(family="Times", size="27", weight="bold")
text_font = tkFont.Font(family="Helvetica", size=14)

# Grid
window.grid_columnfigure(0, weight=1)



window.mainloop()

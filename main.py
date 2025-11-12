import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_BG_COLOR = '#1a1a1a'

FONT_TITLE = ('Arial', 24, 'bold')
FONT_LABEL = ('Arial', 12, 'bold')
FONT_KEY = ('Courier', 14, 'bold')
FONT_BUTTON_GENERATE = ('Arial', 14, 'bold')
FONT_BUTTON_COPY = ('Arial', 10)

COLOR_PRIMARY = '#d4af37'
COLOR_BG = '#1a1a1a'
COLOR_TEXT_WHITE = 'white'
COLOR_ENTRY_BG = '#2d2d2d'
COLOR_ENTRY_FG = '#d4af37'
COLOR_BUTTON_GENERATE_BG = '#d4af37'
COLOR_BUTTON_GENERATE_FG = 'black'
COLOR_BUTTON_COPY_BG = '#000000'
COLOR_BUTTON_COPY_FG = '#000000'

IMAGE_PATH = "ELDEN_RING.jpg"
IMAGE_WIDTH = 400
IMAGE_HEIGHT = 200

KEY_PARTS_COUNT = 3
DIGITS_PER_BLOCK = 2
LETTERS_PER_BLOCK = 3


def generate_key():
    key_parts = []
    
    for _ in range(KEY_PARTS_COUNT):
        digits = [random.choice(string.digits) for _ in range(DIGITS_PER_BLOCK)]
        letters = [random.choice(string.ascii_uppercase) for _ in range(LETTERS_PER_BLOCK)]
        
        block_chars = digits + letters
        random.shuffle(block_chars)
        
        block = ''.join(block_chars)
        key_parts.append(block)
    
    full_key = '-'.join(key_parts)
    key_var.set(full_key)


def copy_to_clipboard():
    key = key_var.get()
    if key:
        root.clipboard_clear()
        root.clipboard_append(key)
        root.update()
        
        messagebox.showinfo("Успех", "Ключ скопирован в буфер обмена!")
    else:
        messagebox.showwarning("Предупреждение", "Сначала сгенерируйте ключ!")


root = tk.Tk()
root.title("Elden Ring Key Generator by Dasha Abramova")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg=WINDOW_BG_COLOR)

main_frame = tk.Frame(root, bg=WINDOW_BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True)

title_label = tk.Label(
    main_frame,
    text="ELDEN RING KEY GENERATOR",
    font=FONT_TITLE,
    fg=COLOR_PRIMARY,
    bg=COLOR_BG
)
title_label.pack(pady=20)

image_frame = tk.Frame(main_frame)
image_frame.pack(pady=10)

image = Image.open(IMAGE_PATH)
image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(image_frame, image=photo)
image_label.image = photo
image_label.pack()

key_var = tk.StringVar()

key_frame = tk.Frame(main_frame, bg=COLOR_BG)
key_frame.pack(pady=20)

tk.Label(
    key_frame,
    text="Сгенерированный ключ:",
    font=FONT_LABEL,
    fg=COLOR_TEXT_WHITE,
    bg=COLOR_BG
).pack()

key_entry = tk.Entry(
    key_frame,
    textvariable=key_var,
    font=FONT_KEY,
    width=25,
    justify='center',
    state='readonly',
    bg=COLOR_ENTRY_BG,
    fg=COLOR_ENTRY_FG
)
key_entry.pack(pady=10)

generate_btn = tk.Button(
    main_frame,
    text="СГЕНЕРИРОВАТЬ КЛЮЧ",
    font=FONT_BUTTON_GENERATE,
    bg=COLOR_BUTTON_GENERATE_BG,
    fg=COLOR_BUTTON_GENERATE_FG,
    command=generate_key,
    padx=20,
    pady=10
)
generate_btn.pack(pady=20)

copy_btn = tk.Button(
    main_frame,
    text="КОПИРОВАТЬ",
    font=FONT_BUTTON_COPY,
    bg=COLOR_BUTTON_COPY_BG,
    fg=COLOR_BUTTON_COPY_FG,
    command=copy_to_clipboard,
    padx=15,
    pady=5
)
copy_btn.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()
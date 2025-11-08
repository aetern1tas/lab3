import tkinter as tk
from tkinter import messagebox
import random
import string
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Elden Ring Key Generator by Dasha Abramova")
root.geometry("800x600")
root.configure(bg='#1a1a1a')


main_frame = tk.Frame(root, bg='#1a1a1a')
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


title_label = tk.Label(
    main_frame,
    text="ELDEN RING KEY GENERATOR",
    font=('Arial', 24, 'bold'),
    fg='#d4af37',
    bg='#1a1a1a'
)
title_label.pack(pady=20)


image_frame = tk.Frame(main_frame, bg='#1a1a1a')
image_frame.pack(pady=10)

image = Image.open("ELDEN_RING.jpg")
image = image.resize((400, 200))
photo = ImageTk.PhotoImage(image)

image_label = tk.Label(image_frame, image=photo, bg='#1a1a1a')
image_label.image = photo
image_label.pack()


key_var = tk.StringVar()


key_frame = tk.Frame(main_frame, bg='#1a1a1a')
key_frame.pack(pady=20)

tk.Label(
    key_frame,
    text="Сгенерированный ключ:",
    font=('Arial', 12, 'bold'),
    fg='white',
    bg='#1a1a1a'
).pack()

key_entry = tk.Entry(
    key_frame,
    textvariable=key_var,
    font=('Courier', 14, 'bold'),
    width=25,
    justify='center',
    state='readonly',
    bg='#2d2d2d',
    fg='#d4af37',
    relief='flat',
    bd=2
)
key_entry.pack(pady=10)

def generate_key():
    key_parts = []
    
    for _ in range(3):
        digits = [random.choice(string.digits) for _ in range(2)]
        letters = [random.choice(string.ascii_uppercase) for _ in range(3)]
        
        block_chars = digits + letters
        random.shuffle(block_chars)
        
        block = ''.join(block_chars)
        key_parts.append(block)
    
    full_key = '-'.join(key_parts)
    key_var.set(full_key)
    
    generate_btn.configure(bg='#f0c050')
    root.after(200, lambda: generate_btn.configure(bg='#d4af37'))

def copy_to_clipboard():
    key = key_var.get()
    if key:
        root.clipboard_clear()
        root.clipboard_append(key)
        root.update()
        
        copy_btn.configure(text="СКОПИРОВАНО!", bg='#4CAF50')
        root.after(1000, lambda: copy_btn.configure(text="КОПИРОВАТЬ", bg="#ef3b65"))
        
        messagebox.showinfo("Успех", "Ключ скопирован в буфер обмена!")
    else:
        messagebox.showwarning("Предупреждение", "Сначала сгенерируйте ключ!")


generate_btn = tk.Button(
    main_frame,
    text="СГЕНЕРИРОВАТЬ КЛЮЧ",
    font=('Arial', 14, 'bold'),
    bg='#d4af37',
    fg='black',
    command=generate_key,
    relief='raised',
    bd=3,
    padx=20,
    pady=10
)
generate_btn.pack(pady=20)


copy_btn = tk.Button(
    main_frame,
    text="КОПИРОВАТЬ",
    font=('Arial', 10),
    bg="#010000",
    fg='white',
    command=copy_to_clipboard,
    relief='flat',
    padx=15,
    pady=5
)
copy_btn.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()
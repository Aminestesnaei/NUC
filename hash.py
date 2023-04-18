import hashlib
from tkinter import *
import base64
import base58
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("System")


def encode():

    out_text64.delete(1.0, END)
    out_text58.delete(1.0, END)
    out_text256.delete(1.0, END)
    out_text256.delete(1.0, END)
    non_encodede256 = text.get("1.0 ", "end-1c").encode()
    none_encoded = text.get("1.0", "end-1c").encode()
    non_encoded58 = text.get("1.0", "end-1c").encode()
    text_encoded256 = hashlib.sha256(non_encodede256).hexdigest()
    text_encoded = base64.b64encode(none_encoded).decode()
    text_encoded54 = base58.b58encode(non_encoded58).decode()

    out_text64.insert('insert', text_encoded)
    out_text58.insert('insert', text_encoded54)
    out_text256.insert('insert', text_encoded256)


def decode():
    global text_decoded
    global img_f
    global image

    out_text64.delete(1.0, END)
    encoded_text = text.get(1.0, END)
    encoded_text.encode()
    text_decoded = base64.b64decode(encoded_text).decode()
    out_text64.insert('insert', text_decoded)


def decode_base58():

    out_text58.delete(1.0, END)
    encoded_text = text.get(1.0, END)
    encoded_text.encode()
    text_decoded58 = base58.b58decode(encoded_text).decode()
    out_text58.insert('insert', text_decoded58)


def clear_in():
    text.delete(1.0, END)
    out_text64.delete(1.0, END)
    out_text58.delete(1.0, END)
    out_text256.delete(1.0, END)


def copy_button64():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(out_text64.get("1.0", "end-1c"))
    clip.destroy()


def copy_button58():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(out_text58.get("1.0", "end-1c"))
    clip.destroy()


def paste_button():
    kb = Tk()
    kb.withdraw()
    text.delete(1.0, END)
    pasted = kb.clipboard_get()
    text.insert('insert', pasted)

    kb.destroy()


def copy_button256():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(out_text256.get("1.0", "end-1c"))
    clip.destroy()


def decode256():
    messagebox.showinfo("ERROR", "SHA 256 is one way compression ")



def root():
    global text
    global out_text64
    global out_text58
    global out_text256
    global root
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    root.title(":))")
    root.geometry("600x800")
    root.resizable(width=True, height=True)
    first = "N U C "
    firsta = Label(root, text=first, font=("", 30))
    firsta.place(x=800, y=30)

    text_to_encode = "To Encode and Decode :"
    a = Label(root, text=text_to_encode, font=("irjadid", 15))
    a.place(x=20, y=50, )

    text_base64 = "Base 64 :"
    base62 = Label(root, text=text_base64, font=("irjadid", 20))
    base62.place(x=32, y=460)

    text_base58 = "Base 58 :"
    base58 = Label(root, text=text_base58, font=("irjadid", 20))
    base58.place(x=32, y=580)

    text_sha256 = "HASH 256 :"
    sha256 = Label(root, text=text_sha256, font=("irjadid", 20))
    sha256.place(x=32, y=700)

#    Buttons

    en_btn = customtkinter.CTkButton(master=root,text="Encode to All !", corner_radius=10, command=encode,)
    en_btn.pack()
    en_btn.place(x=800, y=190)
    de_btn = customtkinter.CTkButton(text="Decode 64", corner_radius=10, command=decode,)
    de_btn.pack()
    de_btn.place(x=950, y=150)
    de58_btn = customtkinter.CTkButton(text="Decode 58", corner_radius=10, command=decode_base58)
    de58_btn.pack()
    de58_btn.place(x=950, y=190)
    de256_btn = customtkinter.CTkButton(text="Decode 256", corner_radius=10, command=decode256)
    de256_btn.pack()
    de256_btn.place(x=950, y=230)
    clearin = customtkinter.CTkButton(text="Clear", corner_radius=10, height=50, width=200,  command=clear_in,)
    clearin.place(x=550, y=290)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, command=copy_button64,)
    copy_btn.place(x=800, y=522)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, command=copy_button58,)
    copy_btn.place(x=800, y=640)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, command=copy_button256,)
    copy_btn.place(x=800, y=760)
    paste_btn = customtkinter.CTkButton(text="Paste", corner_radius=10, height=50, width=200, command=paste_button)
    paste_btn.place(x=150, y=290)

    # input and output TEXT

    text = Text(root, width=50, height=4, font=('irjadid', 20))
    text.pack()
    text.place(x=32, y=140)
    out_text64 = Text(root, width=50, height=2, font=('irjadid', 20))
    out_text64.pack()
    out_text64.place(x=32, y=500)
    out_text58 = Text(root, width=50, height=2, font=('irjadid', 20))
    out_text58.pack()
    out_text58.place(x=32, y=620)
    out_text256 = Text(root, width=50, height=2, font=('irjadid', 20))
    out_text256.pack()
    out_text256.place(x=32, y=740)
    root.mainloop()

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root()

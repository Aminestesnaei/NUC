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

    encoded_text = out_text64.get(1.0, END)
    try:

        encoded_text.encode()
        text_decoded = base64.b64decode(encoded_text).decode()

    
        out_text64.delete(1.0, END)
        out_text64.insert('insert', text_decoded)

    except:
        out_text64.delete(1.0, END)
        out_text64.insert('insert', "Error : that was not Type of base64 ")        

def decode_base58(): 
    
    encoded_text = out_text58.get(1.0, END)
    try:

        encoded_text.encode()
        text_decoded58 = base58.b58decode(encoded_text).decode()
        out_text58.delete(1.0, END)
        out_text58.insert('insert', text_decoded58)
    except:
        out_text58.delete(1.0, END)
        out_text58.insert('insert', "ERROR : That was not Type of Base58")



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


def paste58():
    global out_text58
    kb58 = Tk()
    kb58.withdraw()
    out_text58.delete(1.0, END)
    pasted = kb58.clipboard_get()
    out_text58.insert('insert', pasted)

    kb58.destroy()


def paste64():
    global out_text64
    kb65 = Tk()
    kb65.withdraw()
    out_text64.delete(1.0, END)
    pasted = kb65.clipboard_get()
    out_text64.insert('insert', pasted)

    kb65.destroy()


def root():
    global text
    global out_text64
    global out_text58
    global out_text256
    global root
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    root.title("SGkgOkQ=")
    root.geometry("660x800")
    root.resizable(width=False, height=False)
    first = "N U C "
    firsta = Label(root, text=first, font=("", 20))
    firsta.place(x=250, y=10)

    text_to_encode = "To Encode and Decode :"
    a = Label(root, text=text_to_encode, font=("irjadid", 15))
    a.place(x=20, y=80)

    text_base64 = "Base 64 :"
    base62 = Label(root, text=text_base64, font=("irjadid", 15))
    base62.place(x=20, y=360)

    text_base58 = "Base 58 :"
    base58 = Label(root, text=text_base58, font=("irjadid", 15))
    base58.place(x=20, y=490)

    text_sha256 = "HASH 256 :"
    sha256 = Label(root, text=text_sha256, font=("irjadid", 15))
    sha256.place(x=20, y=620)

    #    Buttons

    en_btn = customtkinter.CTkButton(master=root, text="Encode to All !", corner_radius=10, height=1, command=encode, )
    en_btn.pack()
    en_btn.place(x=500, y=129)
    de_btn = customtkinter.CTkButton(text="Decode 64", corner_radius=10, height=1, command=decode, )
    de_btn.pack()
    de_btn.place(x=500, y=415)
    de58_btn = customtkinter.CTkButton(text="Decode 58", corner_radius=10, height=1, command=decode_base58)
    de58_btn.pack()
    de58_btn.place(x=500, y=545)
    de256_btn = customtkinter.CTkButton(text="Decode 256", corner_radius=10, height=1, command=decode256)
    de256_btn.pack()
    de256_btn.place(x=500, y=675)
    clearin = customtkinter.CTkButton(text="Clear", corner_radius=10, height=50, width=150, command=clear_in, )
    clearin.place(x=300, y=270)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, height=1, command=copy_button64, )
    copy_btn.place(x=500, y=445)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, height=1, command=copy_button58, )
    copy_btn.place(x=500, y=575)
    copy_btn = customtkinter.CTkButton(text="Copy ", corner_radius=10, height=1, command=copy_button256, )
    copy_btn.place(x=500, y=705)
    paste_btn = customtkinter.CTkButton(text="Paste", corner_radius=10, height=50, width=150, command=paste_button)
    paste_btn.place(x=70, y=270)
    paste_btn = customtkinter.CTkButton(text="Paste", corner_radius=10, height=1, width=150, command=paste64)
    paste_btn.place(x=300, y=365)
    paste_btn = customtkinter.CTkButton(text="Paste", corner_radius=10, height=1, width=150, command=paste58)
    paste_btn.place(x=300, y=495)

    # input and output TEXT

    text = Text(root, width=30, height=4, font=('irjadid', 20))
    text.pack()
    text.place(x=32, y=120)
    out_text64 = Text(root, width=30, height=2, font=('irjadid', 20))
    out_text64.pack()
    out_text64.place(x=32, y=405)
    out_text58 = Text(root, width=30, height=2, font=('irjadid', 20))
    out_text58.pack()
    out_text58.place(x=32, y=535)
    out_text256 = Text(root, width=30, height=2, font=('irjadid', 20))
    out_text256.pack()
    out_text256.place(x=32, y=665)
    root.mainloop()


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root()

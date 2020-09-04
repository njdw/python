import random
from tkinter import *
from tkinter import messagebox

text = "abcdefghijklmnopqrstuvwxyz0123456789"
window = Tk()
window.title("Captcha Box by Neil")
window.geometry("300x100")
captcha = StringVar()
user_input = StringVar()

def self_captcha():
	s = random.choices(text, k = 4)
	captcha.set(''.join(s))

def check():
	if captcha.get() == user_input.get():
		messagebox.showinfo("Success", "Correct")
	else:
		messagebox.showerror("Error","Try Again")
	self_captcha()

Label(window,textvariable = captcha,
	font = "Arial 16 bold").pack()
Entry(window,textvariable = user_input,
	font = "Arial 16 bold").pack(ipady = 5)
Button(window,command = check,text = "Check",
	font = "Arial 10").pack()

self_captcha()
window.mainloop()
from tkinter import *

window = Tk()
window.title("Register a Dym domain now for free!")

Label(window, text="Register a Dym domain now for free!").grid(row=0, column=1)
Label(window, text="Enter a domain name you want:").grid(row=1, column=0)
domainName = Entry(window)
domainName.grid(row=1, column=1)

window.mainloop()
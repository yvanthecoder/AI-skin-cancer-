from tkinter import *

window = Tk()
window.title ("CancerClassifier")
window.geometry("720x480")
window.minsize(480, 360)

window.config (background="#98E2C6")

label_title = Label(window, text="Bienvenue sur l'application", font = ("Helvetica", 25), bg='#41B77F', fg='white')
label_title.pack()
window.mainloop()
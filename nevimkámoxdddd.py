from tkinter import *


window =  Tk()
window.title("Tvoje mama")
window.configure(width = 500, height = 300)
window.configure(bg ='lightgray')

button = Button(window, text="Tvoje mama xdd", fg = 'black')
button.place(x = 80, y = 100)

lbl = Label(window, text= "SUS", fg= 'black', font=("Comic Sans", 16))
lbl.place(x = 100, y = 50)

winWidth = window.winfo_reqwidth()
winHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenheight() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))

window.mainloop()
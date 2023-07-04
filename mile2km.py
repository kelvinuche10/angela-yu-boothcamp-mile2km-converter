from tkinter import *

window = Tk()
window.title('Mile to Kilometer converter')
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


def calculate():
	km = float(entry.get()) * 1.604
	km_no.config(text=km)

entry = Entry()
entry.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)

equals = Label(text='is equal to')
equals.grid(column=0, row=1)

km_no = Label(text='0')
km_no.grid(column=1, row=1)

km = Label(text='km')
km.grid(column=2, row=1)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)






window.mainloop()
# import tkinter

# window = tkinter.Tk()
# window.title('My first GUI program')
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text='my first label', font=('Arail', 24, 'bold'))
# my_label.pack(side='left ')









# window.mainloop()


def add(*args):
	sum = 0
	for n in args:
		sum += n
	return sum

print(add(2, 3, 4, 5, 6, 6))

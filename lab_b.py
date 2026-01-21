from tkinter import Tk, Frame, Label, Button, Entry, messagebox
window = Tk()
window.title('Hello')
frame = Frame(window)
Label(frame, text="Mikä on sinun nimesi? ", padx=10, pady=10).pack(side='left')
entry = Entry(frame)
entry.pack(side='right')
frame.pack(side='top')
Button(window, text='Lähetä',
command=lambda: [messagebox.showinfo("Hello",
f'Hauska tavata, {entry.get()}!'),
entry.delete(0, 'end')]
).pack(side='bottom')
window.mainloop()

from tkinter import *

root = Tk()
root.title('Learn')

r = IntVar()

Radiobutton(root, text="Option 1", variable=r, value=2).pack()
Radiobutton(root, text="Option 2", variable=r, value=2).pack()
Radiobutton(root, text="Option 3", variable=r, value=3).pack()
Radiobutton(root, text="Option 4", variable=r, value=3).pack()
root.geometry(540 * 600,)






mainloop()
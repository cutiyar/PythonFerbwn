from tkinter import *
from tkinter import ttk
root = Tk()
entry1 = ttk.Entry(root, width=40)  # Eme bo texts bekardet wate keseke shteky tya bnwset
entry1.pack()  # pack eshy tatbyqkrdna la naw root
login=PhotoImage(file='Circles-3.gif')
resize_login=login.subsample(100,100)
bu1 = ttk.Button(root, text="Get text")  # lere dwgmayak drwst dekey be nawt get text
bu1.pack()
bu1.config(image=login,compound=CENTER)
def buclick():
    print(entry1.get())  # eme le katy krte krdnda esh dekat w printy nwsyneke dekat. wate zanyaryekany naw entry1 werdegret.
    entry1.delete(0, END)  # Lere pey delleyn her shtek ke nwsra dway awa la xanaka bysrrawa la 0 ta kotayy.
bu1.config(command=buclick)  # eme bo ewey buclick bbestynewe be bu1 .
root.mainloop()

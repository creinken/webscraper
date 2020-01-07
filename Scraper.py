import ttk
from Tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Web Scraper")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        file = Menu(menu)

        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)

        optionsWindow = Frame(self, relief=RAISED, width=500, borderwidth=1)
        optionsWindow.grid_propagate(0)
        tabsWindow = Frame(self)

        optionsWindow.pack(fill=Y, side=LEFT, anchor=W, expand=False)
        tabsWindow.pack(fill=BOTH, side=RIGHT, expand=True)

        singleURLLabel = ttk.Label(optionsWindow, text='URL to Scrape:')
        singleURLLabel.grid(row=0, column=0)
        singleURL = StringVar()
        singleURLToScrape = Entry(optionsWindow, textvariable=singleURL)
        singleURLToScrape.grid(row=0, column=1, columnspan=4)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("900x500")

app = Window(root)

root.mainloop()
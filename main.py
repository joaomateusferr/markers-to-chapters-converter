import os
from tkinter import *
from tkinter import filedialog

def run():

    FilePath = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("csv files", "*.csv"),("all files", "*.*")))
    ResultLabel.configure(text=str(FilePath))
    ResultLabel.pack()
    #FileSelectorButton.destroy()
    os.startfile(str(FilePath))

MainWindow = Tk()
MainWindow.title("Convert DaVinci Resolve markers to YouTube chapters")
MainWindow.geometry("400x400")

MainFrame = Frame()
ResultLabel = Label(MainFrame, text="")
FileSelectorButton = Button(MainFrame, text="Click Me", command=run)

MainFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
FileSelectorButton.pack()

MainWindow.mainloop()
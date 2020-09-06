from tkinter import Toplevel, Label
import fonts


def showError(location,panel) :

    errorWindow = Toplevel(panel)
    errorWindow.title("not found")
    errorWindow.geometry("400x50")
    errorWindow.resizable(0,0)
    errorWindow.configure(bg='white')
    errorWindow.iconbitmap('sad-cloud.ico')

    textLabel = Label(errorWindow, text='We are sorry, we could not find {} '.format(location), font=(fonts.errorFont))
    textLabel.configure(bg='white')
    textLabel.pack()


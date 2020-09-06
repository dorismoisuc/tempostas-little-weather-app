from tkinter import *
from PIL import ImageTk, Image

from fonts import *
from tempostasAPI import get_weather
from tkinter import messagebox
from showErrorFct import showError

'''
THE ROOT OF THE APP
'''

tempostas = Tk()
tempostas.title("t e m p o s t a s ")



background = ImageTk.PhotoImage(Image.open("tempo.jpg"))

panel = Label(tempostas,image=background)

panel.pack(side='bottom',fill='both',expand='yes')

tempostas.iconbitmap('tempoico.ico')

tempostas.geometry("540x720")

tempostas.resizable(0,0)

'''
DONE
'''

'''
next elements: 
- text entry for searching the location
- search button
- location label (location's name, location's country)
- temperature in celsius, kelvin, and fahrenheit
- main description of the 'atmospheric' weather
- secondary description 
'''

locationText = StringVar()
locationEntry = Entry(panel,textvariable=locationText,font=(locationEntryFont))
locationEntry.configure(background='white')
locationEntry.pack(pady=20)



def search():
    location = locationEntry.get()
    weather = get_weather(location)
    if weather:
        locationLabel['text']='{}, {}'.format(weather[0],weather[1])
        temperatureLabel['text']='{:.2f}°C, {:.2f}°K, {:.2f}°F'.format(weather[2],weather[3],weather[4])
        mainDescription['text']=weather[5]
        secondaryDescription['text']=weather[6]
    else:
        showError(location,panel)


searchButton = Button(panel,text='Search weather for your location', width=30,command = search,font=(searchButtonFont))
searchButton.configure(background='white')
searchButton.pack(pady=20)

locationLabel = Label(panel, text='Location',font=(locationLabelFont))
locationLabel.configure(background='white')
locationLabel.pack()

temperatureLabel = Label(panel,text='Temperature in °C, °K, °F',font=(temperatureFont))
temperatureLabel.configure(background='white')
temperatureLabel.pack(pady=20)

mainDescription = Label(panel,text='Main weather description',font=(mainDescriptionFont))
mainDescription.configure(background='white')
mainDescription.pack(pady=20)

secondaryDescription = Label(panel,text='Secondary weather description',font=(secondaryDescriptionFont))
secondaryDescription.configure(background='white')
secondaryDescription.pack()

def open_new():
    newWindow = Toplevel(panel)
    newWindow.title("info for tempostas")
    newWindow.geometry("500x200")
    newWindow.configure(bg='white')
    newWindow.iconbitmap('infoicon.ico')
    tempostasDescription = Label(newWindow, text="Hello ☻ \n TEMPOSTAS will provide you the weather conditions\n from all across the world. \n"
                                                 "You just have to enter a location, \nand the temperature in celsius, kelvin, and fahrenheit\n"
                                                 "will be shown. \n and also 2 short atmospheric descriptions.\n Enjoy! ",font=(newWindowTextFont))
    tempostasDescription.configure(bg='white')
    tempostasDescription.configure(fg='gray')
    tempostasDescription.pack()


newWindowButton = Button(panel,text='Click for more info',width=18,command=open_new,font=(newWindowFont))
newWindowButton.configure(background='blue')
newWindowButton.pack(pady=100)

tempostas.mainloop()
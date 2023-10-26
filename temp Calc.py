from tkinter import *


def buttonPress(num):
    global equationText
    equationText += str(num)
    equationLabel.set(equationText)

def backspace():
    global equationText
    equationText = equationText[:-1]
    equationLabel.set(equationText)

def clear():
    global equationText
    equationText = ""
    equationLabel.set(equationText)

def toFahrenheit():
    global equationText
    global fahrenheit

    try:

        fahrenheit = float(equationText)
        fahrenheit = (fahrenheit * 1.8) + 32
        fahrenheit = str(fahrenheit)

        equationText = fahrenheit
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("no num entered/syntax error")
    except SyntaxError:
        equationLabel.set("syntax error")

def toCelsius():

    try:

        global equationText
        global celsius

        celsius = float(equationText)
        celsius = (celsius - 32) * 5 / 9
        celsius = str(celsius)

        equationText = celsius
        equationLabel.set(celsius)
    except ValueError:
        equationLabel.set("no num entered/syntax error")
    except SyntaxError:
        equationLabel.set("syntax error")

def cToKelvin():
    try:
        global equationText
        global kelvin

        kelvin = float(equationText)
        kelvin = kelvin + 273.15
        kelvin = str(kelvin)

        equationText = kelvin
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("no num entered/syntax error")

def fToKelvin():
    try:
        global equationText
        global kelvin

        kelvin = float(equationText)
        kelvin = (kelvin - 32) * 5 / 9
        kelvin += 273.15
        kelvin = str(kelvin)

        equationText = kelvin
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("no num entered/syntax error")


def KtoCelsius():

    try:
        global equationText
        global celsius

        celsius = float(equationText)
        celsius -= 273.15
        celsius = str(celsius)

        equationText = celsius
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("no num entered/syntax error")

def KtoFahrenheit():
    try:
        global equationText
        global fahrenheit

        fahrenheit = float(equationText)
        fahrenheit = (fahrenheit - 273.15) * 9/5 + 32
        fahrenheit = str(fahrenheit)

        equationText = fahrenheit
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("no num entered/syntax error")

def plusMinus():
    try:
        global equationText
        global convert

        convert = float(equationText)
        convert = 0 - convert
        convert = str(convert)

        equationText = convert
        equationLabel.set(equationText)
    except ValueError:
        equationLabel.set("value error")





window = Tk()
window.title("Temp Calculator")
window.geometry("700x500")
window.config(bg = "#000000")

equationText = ""
equationLabel = StringVar()

label = Label(window, textvariable=equationLabel, font=('Calibri',20), bg="white", width=48, height=2)
label.pack()

frame = Frame(window)
frame.pack()


class buttons:
    button7 = Button(frame, text=7, width=8, height=4, font=35, command=lambda:buttonPress(7))
    button7.grid(row=0, column=0)

    button8 = Button(frame, text=8, width=8, height=4, font=35, command=lambda:buttonPress(8))
    button8.grid(row=0, column=1)

    button9 = Button(frame, text=9, width=8, height=4, font=35, command=lambda:buttonPress(9))
    button9.grid(row=0, column=2)

    button4 = Button(frame, text=4, width=8, height=4, font=35, command=lambda:buttonPress(4))
    button4.grid(row=1,column=0)

    button5 = Button(frame, text=5, width=8, height=4, font=35, command=lambda:buttonPress(5))
    button5.grid(row=1,column=1)

    button6 = Button(frame, text=6, width=8, height=4, font=35, command=lambda:buttonPress(6))
    button6.grid(row=1,column=2)

    button1 = Button(frame, text=1, width=8, height=4, font=35, command=lambda:buttonPress(1))
    button1.grid(row=2,column=0)

    button2 = Button(frame, text=2, width=8, height=4, font=35, command=lambda:buttonPress(2))
    button2.grid(row=2,column=1)

    button3 = Button(frame, text=3, width=8, height=4, font=35, command=lambda:buttonPress(3))
    button3.grid(row=2,column=2)

    button0 = Button(frame, text=0, width=8, height=4, font=35, command=lambda:buttonPress(0))
    button0.grid(row=3,column=0)

    buttonDec = Button(frame, text=".", width=8, height=4, font=35, command=lambda:buttonPress("."))
    buttonDec.grid(row=3,column=1)

    backspace = Button(frame, text = "←", width=8, height=4, font=35, command=backspace)
    backspace.grid(row=3,column=2)

    clear = Button(window, text = "C", width=16, height=4, font=35, command=clear)
    clear.pack()

    toF = Button(frame, text = "°C  →  °F", width = 16, height = 4, font=35, command=toFahrenheit)
    toF.grid(row=0, column=3)

    toC = Button(frame, text = "°F  →  °C", width = 16, height = 4, font=35, command=toCelsius)
    toC.grid(row=1, column=3)

    ctok = Button(frame, text = "°C  →  K", width=16, height=4, font=35, command=cToKelvin)
    ctok.grid(row=2, column=3)

    ftok = Button(frame, text = "°F  →  K", width=16, height=4, font=35, command=fToKelvin)
    ftok.grid(row=3, column=3)

    ktoc = Button(frame, text = "K  →  °C", width=16, height=4, font=35, command=KtoCelsius)
    ktoc.grid(row=0, column=4)

    
    ktof = Button(frame, text = "K  →  °F", width=16, height=4, font=35, command=KtoFahrenheit)
    ktof.grid(row=1, column=4)

    plusMinus = Button(frame, text = "±", width = 16, height = 4, font = 35, command = plusMinus)
    plusMinus.grid(row=2, column=4)



window.mainloop()
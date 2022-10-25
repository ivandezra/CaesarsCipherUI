from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

#alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#decoding function
def decode():
  shiftnumber=int(numberentry.get())
  originaltext=str(textentry.get())
  finaltext=""
  shiftnumber=shiftnumber*(-1)
  for letter in str(originaltext):
    if letter in alphabet:
      position=alphabet.index(letter)
      newposition=position+shiftnumber
      if newposition>25:
        newposition%=26
      elif newposition<0:
        newposition+=26
      finaltext+=alphabet[newposition]
    elif letter.isupper()==True:
      lower=letter.lower()
      position=alphabet.index(lower)
      newposition=position+int(shiftnumber)
      if newposition>25:
        newposition%=26
      elif newposition<0:
        newposition+=26
      finaltext+=alphabet[newposition].upper()
    else:
      finaltext+=letter
  messagebox.showinfo("Result", finaltext)

#encoding function
def encode():
  shiftnumber=int(numberentry.get())
  originaltext=str(textentry.get())
  finaltext=""
  for letter in str(originaltext):
    if letter in alphabet:
      position=alphabet.index(letter)
      newposition=position+int(shiftnumber)
      if newposition>25:
        newposition%=26
      finaltext+=alphabet[newposition]
    elif letter.isupper()==True:
      lower=letter.lower()
      position=alphabet.index(lower)
      newposition=position+int(shiftnumber)
      if newposition>25:
        newposition%=26
      finaltext+=alphabet[newposition].upper()
    else:
      finaltext+=letter
  messagebox.showinfo("Result", finaltext)

#main UI
root = Tk()
root.geometry('700x700')
root.title("Encryption System")
root.config(bg='SteelBlue3')

#header
headingFrame = Frame(root,bg="azure",bd=5)
headingFrame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
headingLabel = Label(headingFrame, text="Welcome to the Encryption System", bg='azure', font=('Helvetica',20,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#text input
Frame1 = Frame(root,bg="SteelBlue3")
Frame1.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

label1 = Label(Frame1,text="Enter the text: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label1.place(relx=0.05,rely=0.2, relheight=0.08)

textentry = Entry(Frame1,font=('Century 12'))
textentry.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#number input
Frame2 = Frame(root,bg="SteelBlue3")
Frame2.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

label2 = Label(Frame2,text="Enter the number of shifts: ",bg="SteelBlue3",fg='azure',font=('Courier',13,'bold'))
label2.place(relx=0.05,rely=0.2, relheight=0.08)

numberentry = Entry(Frame2,font=('Century 12'))
numberentry.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#encode button
button1 = Button(root, text='Encode',font=('Courier',15,'normal'),command=encode)
button1.place(relx=0.35,rely=0.6, relwidth=0.25, relheight=0.05)

#decode button
button2 = Button(root, text='Decode',font=('Courier',15,'normal'),command=decode)
button2.place(relx=0.35,rely=0.7, relwidth=0.25, relheight=0.05)

root.mainloop()

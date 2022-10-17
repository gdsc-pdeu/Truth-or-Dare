#importing questions
from tkinter.font import BOLD
import pandas as pd
t_data=pd.read_csv("Truth.csv")
t_q=list(t_data.iloc[:,1].values)
d_data=pd.read_csv("Dare.csv")
d_q=list(d_data.iloc[:,1].values)


import tkinter , Questions
win1=tkinter.Tk()          #Handle
win1.geometry("1193x671")  #Size of the window


class Truth():
    def __init__(self):
        self.win2 = tkinter.Tk()
        self.win2.geometry('1800x540')
        label = tkinter.Label(self.win2, text=(Questions.truth_question(t_q)), pady=250, padx=100, bg='#faeadd',fg='brown', font=("Helvetica", "30", "bold"))
        label.pack(expand=True,fill=tkinter.X)
        back = tkinter.Button(self.win2, text='Back',padx=100, pady=10, bg='white', command=self.quit)
        back.place(x=620,y=490)
        self.win2.mainloop()

    def quit(self):
        self.win2.destroy()


class Dare():
    def __init__(self):
        self.win2 = tkinter.Tk()
        self.win2.geometry('1800x540')
        label = tkinter.Label(self.win2, text=(Questions.dare_question(d_q)), pady=250, padx=100, bg='#faeadd', fg='brown', font=("Helvetica", "30", "bold")) 
        label.pack(expand=True,fill=tkinter.X)
        back = tkinter.Button(self.win2, text='Click and Quit',padx=100,pady=10,bg='white',command=self.quit)
        back.place(x=620,y=490)
        self.win2.mainloop()

    def quit(self):
        self.win2.destroy()


#Main Screen Backgrounds
bg = tkinter.PhotoImage(file = "Back.png")
  

# Show image using label
background = tkinter.Label( win1, image = bg)
background.place(x =0, y = 0)

#Middle line
label1 = tkinter.Label(win1,pady=1000,bg="black")
label1.place(x=600)

label2 = tkinter.Label(win1, text="What Do You Pick?",bg="#faeadd", font=("Helvetica", "55", "bold"))
label2.place(x=210,y=160)

#Buttons
Truth = tkinter.Button(win1, text="Truth", command=Truth,pady=10,padx=70,bg="brown",font=("Helvetica", "20","bold")) 
Truth.config(fg="white")
Truth.place(x=250,y=400)

Dare  = tkinter.Button(win1, text="Dare" , command=Dare,pady=10,padx=70,bg="pink",font=("Helvetica", "20","bold")) 
Dare.place(x=700,y=400)

win1.mainloop()

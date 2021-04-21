#tkinter daily planner app
#generates a window which, in one frame reads in activity, start, end times
#second from displays the list of activities
#gets the current YYYY-mm-dd
#stores daily plan in YYYY-mm-dd.txt file
#when 'finished?' button is activated GUI window closes and 

from tkinter import *
from datetime import datetime
import os

class inputDisplayText:
    def __init__(self):
        self.window =Tk()
        self.window.title("Daily Planner")
        frame1=Frame(self.window)
        frame1.pack()

        self.v1=StringVar()
        self.v2=StringVar()
        self.v3=StringVar()
        act_label=Label(frame1,text="Activity")
        act_entry =Entry(frame1,textvariable=self.v1,width=50)

        start_label=Label(frame1,text="Start Time")
        start_entry=Entry(frame1,textvariable=self.v2)

        end_label = Label(frame1, text="End Time")
        end_entry=Entry(frame1,textvariable=self.v3)
        
        button_sub = Button(frame1,text="Submit",command=self.displayText)
        button_fin = Button(frame1,text="Finished?",command=self.finished)

        act_label.grid(row=1,column=1)
        act_entry.grid(row=1,column=2)
        start_label.grid(row=2,column=1)
        start_entry.grid(row=2,column=2)
        end_label.grid(row=3,column=1)
        end_entry.grid(row=3,column=2)

        button_sub.grid(row=4,column=2)
        button_fin.grid(row=5,column=2)

        frame2=Frame(self.window)
        frame2.pack()
        label=Label(frame2,text="Today's Plan")
        label.grid(row=1,column=1)
        self.text= Text(self.window)
        self.text.pack()
        self.text.insert(END,"A display of your planned activities")
        self.window.mainloop()

    def displayText(self):
        self.text.insert(END, '\n')
        self.text.insert(END,self.v1.get())
        self.text.insert(END, '\t')
        self.text.insert(END, self.v2.get())
        self.text.insert(END, '\t')
        self.text.insert(END, self.v3.get())

        f.write(str(self.v1.get())+'\t'+str(self.v2.get())+'\t'+str(self.v3.get())+'\n')
        #print(myList)

    def finished(self):
        f.close()
        self.window.destroy()
#gets the current YYYY-mm-dd
#stores daily plan in YYYY-mm-dd.txt file

todaysDate=datetime.today().strftime('%Y-%m-%d')
fileName = todaysDate+'.txt'
if os.path.isfile(fileName)== True:
    os.remove(fileName)
f=open(fileName,"a")
myList=[]
inputDisplayText()
        

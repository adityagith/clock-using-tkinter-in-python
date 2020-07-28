from tkinter import *

def at():
    i = 0
    for i in range(0,60):
        for j in range(0,60):
            for k in range(0,10000):
                intvalue.set(i)
                ina.update()
                pass

root = Tk()

root.geometry("250x165")

frame = Frame(root,bg="black")

#label1 = Label(frame,text="ok",bg="red",font="Verdana 90")

#label1.pack(expand=True,fill="both")



frame.grid(column=1)


frame1 = Frame(root,bg="red")

frame1.grid(column=2,row=0)

#label2 = Label(frame1,text="pk",bg="green",font="Verdana 90")

#label2.pack()

frame2 = Frame(root,bg="blue")
frame2.grid(column=1,row=1)


a = IntVar()
b = IntVar()
c = StringVar()


minute = Entry(frame,textvariable=a,bg="red",font="Verdana 50",width=3)
second = Entry(frame1,textvariable=b,bg="red",font="Verdana 50",width=3)

day = Entry(frame2,textvariable=c,bg="red",font="Verdana 50",width=3)

c.set("Mo")
day.update()
        
minute.pack()
second.pack()
day.pack()



for i in range(0,60):
    for j in range(0,60):
        for k in range(0,10000):
            a.set(i)
            b.set(j)
            minute.update()
            second.update()
            pass
        

root.mainloop()

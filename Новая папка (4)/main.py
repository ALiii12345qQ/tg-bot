from tkinter import *

root = Tk()

root.title("Приложение")
root.geometry("700x500")

frame = Frame(root)
frame.pack(anchor='center')

def calculate():
    
    
    val = ent1.get()
    valC1 = ent2.get()
    val3 = ent3.get()

    if val == '' or val3 == '' or valC1 == '':
        txt["text"] = 'Заполните все поля'
        return
    
    if valC1 == '+':
        txt['text'] =  float(val) + float(val3)
    
    elif valC1 == "*":
        txt['text'] = float(val) * float(val3)
    elif valC1 == "-":
        txt['text'] = float(val) - float(val3)
    elif valC1 == "/":
        txt['text'] = float(val) / float(val3)
    else:
        txt['text'] = "напиши в операторе + - * / "

lab1 = Label(frame, text="Число",font=("Comic Sans MS",19, "bold"))
lab2 = Label(frame, text="Операция",font=("Comic Sans MS",19, "bold"))
lab3 = Label(frame, text="Число",font=("Comic Sans MS",19, "bold"))
ent1 = Entry(frame, font=("Comic Sans MS",19, "bold"), width=10)
ent2 = Entry(frame, font=("Comic Sans MS",19, "bold"), width=10)
ent3 = Entry(frame, font=("Comic Sans MS",19, "bold"), width=10)
btn1 = Button(frame, text="Вычислить",font=("Comic Sans MS",19, "bold"), command=calculate)
txt = Label(frame, text="", font=('Comic Sans MS', 18, "bold"))

lab1.grid(row=0,column=0,padx=10,pady=10)
lab2.grid(row=0,column=1,padx=10,pady=10)
lab3.grid(row=0,column=2,padx=10,pady=10)

ent1.grid(row=1,column=0,padx=10,pady=10)
ent2.grid(row=1,column=1,padx=10,pady=10)
ent3.grid(row=1,column=2,padx=10,pady=10)

btn1.grid(row=2, column=0,columnspan=3,sticky='we',padx=10,pady=10)
txt.grid(row=3,column=0,columnspan=3,sticky='we',padx=10,pady=10)

root.mainloop()
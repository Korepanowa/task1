from tkinter import *
from tkinter import ttk
from tkinter import filedialog 
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import re
from itertools import islice


numbers = []

gui = Tk()
gui.geometry("2000x1000")
gui.title("Объединение файлов .gcode")

#Необходимо для перезаписи координат для вывода 2D изображения объединённого кода
def append_if_different(x, y):
    if not numbers or (x, y) != numbers[-1]:
        numbers.append((x, y))

#Выбор основного файла
def getFile1():
    global filename1
    
    filename1 = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("gcode files", "*.gcode"),("all files","*.*")))
    s.configure(text = "Файл выбран",state = DISABLED)

    showinfo(message='Файл выбран')
    

    
#Выбор второго файла
def getFile2():
    global filename2
    
    filename2 = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("gcode files", "*.gcode"),("all files","*.*")))
    c.configure(text = "Файл выбран", state = DISABLED)
    w.configure(state = NORMAL)
    showinfo( message='Файл выбран')


#Объединение кодов:
def Unification():
    
    
                
     #Удаление не нужных строк из второго файла
        n=30

        with open(filename2) as ipn:
            l = ipn.readlines()

        with open(filename2, 'w') as out:
            out.writelines(l[n:])

     #Удаление не нужных строк из основного файла
        N=38
    
        with open(filename1) as f1:
            lines = f1.readlines()

        with open(filename1, 'w') as f2:
            f2.writelines(lines[:-N])
     #Копирование одного файла в другой
        with open(filename1, 'a') as file1, open(filename2, 'r') as file2 :
            for line in file2:
                file1.write(line)

     #Перенос из кода только координат в отдельный файл

        with open(filename1,"r") as inp:
            for line in inp:
                matches = re.findall(r'[XY]([-+]?\d+)', line)
                if len(matches) == 2:
                    append_if_different(int(matches[0]), int(matches[1]))
     

        with open(filename2, "w") as outp:
            for xy in numbers:
                outp.write("{}\n{}\n".format(*xy))

        
     #Создание изображения по координатам из файла
        with open(filename2, 'r') as f:
           while True:
            l = list(islice(f,4))
            
            x1 = [l[0]]
            y1 = [l[1]]
            x2 = [l[2]]
            y2 = [l[-1]]

            canvas.create_line(x1,y1,x2,y2)

            if not l:
                break

        
        showinfo(message='Выполнено')
    
        
#Действия кнопки для очищения
def clear1():
    s.configure(text = "Выбор основного файла",state = NORMAL)
    c.configure(text = "Выбор второго файла", state = NORMAL)

    filename1 = ' '
    filename2 = ' '
    canvas.delete("all")
    showinfo(message='Очищено')
    

folderPath = StringVar()



s = ttk.Button(gui, text="Выбор основного файла" ,command=getFile1)
s.grid(row=0,column=2)

c = ttk.Button(gui ,text="Выбор второго файла", command=getFile2)
c.grid(row=0,column=4)

w = ttk.Button(gui ,text="Объединение", state = DISABLED, command=Unification)
w.grid(row=0,column=6)

o = ttk.Button(gui ,text="Очистить", command=clear1)
o.grid(row=0,column=7)

canvas = Canvas(bg="white", width=500, height=500)
canvas.grid(row=200,column=6)
 


lb1=Label(text = 'Внимание, убедитесь, что используете копии!!!', font=("Arial Bold", 10) )
lb1.grid(column = 4, row = 70)
gui.mainloop()






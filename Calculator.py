from tkinter import *
from tkinter import messagebox
def Click_button(num):
    global Text
    Text = Text + str(num)
    display_input.set(Text)

def Clear_button():
    global Text
    Text = ""
    display_input.set("")

def Equal_button():
    global Text
    sumup= str(eval(Text))
    Text = ""
    display_input.set(sumup)
    
root = Tk()
root.title("Calculator")
c = Canvas(root , height = 500 , width = 800 , background = "yellow")
line = c.create_line(0 , 20 , 1000 ,20)
line = c.create_line(20 , 0 , 20 , 800)
line = c.create_line(780 , 0 , 780 ,500)
line = c.create_line(0 , 480 , 800 ,480 )
c.pack()

Text = ""
display_input = StringVar()
Heading = Label(root , text = "Calculator" , background = "yellow" , font = ("arial" , 30 , "bold")).place(x = 310 , y = 30)
root.configure(width = 800 , height = 500)
display_box = Entry(root , font = ("arial" , 20 , "bold") , border = 15 , width = 15 ,textvariable = display_input , justify = "right" , bg = "powder blue" , insertwidth = 4).place(x = 500 , y = 150)
_1 = Button(root , border = 2 , text = "1" ,width = 8 ,height = 4 , font = ("arial" , 10,  "bold") ,command = lambda : Click_button(1), bg = "powder blue").place(x = 50 , y = 100)
_2 = Button(root , border = 2 , text = "2" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(2), bg = "powder blue").place(x = 140 , y = 100)
_3 = Button(root , border = 2 , text = "3" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(3), bg = "powder blue").place(x = 230 , y = 100)
_4 = Button(root , border = 2 , text = "4" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(4), bg = "powder blue").place(x = 50 , y = 190)
_5 = Button(root , border = 2 , text = "5" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(5), bg = "powder blue").place(x = 140 , y = 190)
_6 = Button(root , border = 2 , text = "6" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(6), bg = "powder blue").place(x = 230 , y = 190)
_7 = Button(root , border = 2 , text = "7" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(7), bg = "powder blue").place(x = 50 , y = 280)
_8 = Button(root , border = 2 , text = "8" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(8), bg = "powder blue").place(x = 140 , y = 280)
_9 = Button(root , border = 2 , text = "9" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(9), bg = "powder blue").place(x = 230 , y = 280)
_0 = Button(root , border = 2 , text = "0" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button(0), bg = "powder blue").place(x = 50 , y = 370)
_00     = Button(root , border = 2 , text = "00" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("00"), bg = "powder blue").place(x = 140 , y = 370)
_dot    = Button(root , border = 2 , text = "." ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("."), bg = "powder blue").place(x = 230 , y = 370)
_divide = Button(root , border = 2 , text = "/" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("/"), bg = "powder blue").place(x = 320 , y = 100)
_mult   = Button(root , border = 2 , text = "x" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("*"), bg = "powder blue").place(x = 320 , y = 190)
_add    = Button(root , border = 2 , text = "+" ,width = 8 ,height = 10 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("+"), bg = "powder blue").place(x = 320 , y = 275) 
_percent= Button(root , border = 2 , text = "%" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("%"), bg = "powder blue").place(x = 410 , y = 190)
_sub    = Button(root , border = 2 , text = "__" ,width = 8 , height = 4 , font = ("arial" , 10 , "bold") ,command = lambda : Click_button("-"), bg = "powder blue").place(x = 410 , y = 280)
_clear  = Button(root , border = 2 , text = "C" ,width = 8 ,height = 4 , font = ("arial" , 10 , "bold") ,command = Clear_button, bg = "powder blue").place(x = 410 , y = 370)
_equal  = Button(root , border = 2 , text = "=" , width = 8 , height = 4 , font = ("arial" , 10 , "bold") ,command = Equal_button, bg = "powder blue").place(x = 410 , y =100)
root.mainloop()

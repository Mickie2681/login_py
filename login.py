from cgitb import text
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

img = PhotoImage(file = 'login.png')
Label(root, image = img, bg='white' ).place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading = Label(frame,text = 'Signin' , fg = '#57a1f8', bg='white', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=10)

##############
user= Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=25,y=80)
user.insert(0,'Username')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

####################
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#####################_____

Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white', border=0).place(x=35,y=204)
label= Label(frame,text="Don't have an account?",fg='black',bg='white', font=('Microsoft YaHei UI Light',11) )
label.place(x=75,y=270)

sign_up = Button(frame,width= 6,text= 'sign up', border= 0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=150,y=300)
root.mainloop()
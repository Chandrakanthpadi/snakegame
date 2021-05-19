import tkinter as tk
from tkinter import Label
import snakestart

screen = tk.Tk()
screen.title('Snake game')
screen.geometry("400x300+300+200")

f=open('Highscore.txt','r')
hscore = f.read(1)
f.close()
print(hscore)
la = Label(text="Highscore = "+str(hscore),height=10)
la.pack()
start_button = tk.Button(screen,text ='Start',width =20,command = snakestart.gamestart)
start_button.pack()

quit_button = tk.Button(screen,text ='quit',width =20,command = screen.destroy)
quit_button.pack()

f=open('Highscore.txt','r')
hscore = f.read(1)
f.close()

screen.mainloop()
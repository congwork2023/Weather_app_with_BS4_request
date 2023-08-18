from tkinter import Tk
from tkinter import Label
from PIL import Image, ImageTk


master=Tk() #make window
master.title("weather_app") #create title
master.config(bg="white") #Configuration background is white

locationLable=Label(master,font=("Calibri Bold",20),bg="white") #tạo nhãn cho các biến 
temperatureLable= Label(master,font=("Calibri Bold",70),bg="white")#như trên# Font lớn nhất 
weatherprectionLable=Label(master,font=("Calibri Bold",50),bg="white")# như trên#




master.mainloop() #run the window
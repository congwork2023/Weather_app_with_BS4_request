from tkinter import Tk
from tkinter import Label
from PIL import Image, ImageTk # position of logo


master=Tk() #make window
master.title("weather_app") #create title
master.config(bg="white") #Configuration background is white

#position logo
img=Image.open("Img\weather_logo.png")
img=img.resize((150,150))

#add Imamge into object
img_Object =ImageTk.PhotoImage(img)
#create Lable and position of Lable by grid
Label(master, image=img_Object, bg="white").grid(row=1,sticky="E")


locationLable=Label(master,font=("Calibri Bold",20),bg="white") #tạo nhãn cho các biến 
temperatureLable= Label(master,font=("Calibri Bold",70),bg="white")#như trên# Font lớn nhất 
weatherprectionLable=Label(master,font=("Calibri Bold",50),bg="white")# như trên#




master.mainloop() #run the window
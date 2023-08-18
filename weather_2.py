from tkinter import Tk
from tkinter import Label
from PIL import Image, ImageTk # position of logo


window=Tk() #make window (replace master variable to window)
window.title("weather_app") #create title
window.config(bg="white") #Configuration background is white

#position logo
img=Image.open("Img\weather_logo.png")
img=img.resize((150,150))

#add Imamge into object
img_Object =ImageTk.PhotoImage(img)
#create Lable and position of Lable by grid
Label(window, image=img_Object, bg="white").grid(row=1,sticky="E")


locationLable=Label(window,font=("Calibri Bold",20),bg="white") #tạo nhãn cho các biến 
temperatureLable= Label(window,font=("Calibri Bold",70),bg="white")#như trên# Font lớn nhất 
weatherprectionLable=Label(window,font=("Calibri Bold",50),bg="white")# như trên#




window.mainloop() #run the window
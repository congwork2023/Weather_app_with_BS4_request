from tkinter import Tk
from tkinter import Label
from PIL import Image, ImageTk # position of logo

import requests #yêu cầu HTTP 
from bs4 import BeautifulSoup #Phân tích và trích xuất HTML

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

url="https://weather.com/en-CA/weather/today/l/c4877d013a65b996c469bc919c35c1b1af5cb13c0c6868275de92ba1e2a936cb7e6c9b3cf58bb491f3a1347e4d84b14e"
def get_weather() :
    page = requests.get(url)
    soup =BeautifulSoup(page.content,"html.parser")
    location=soup.find("h1",class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find ("span", class_ = "CurrentConditions--tempValue--MHmYY").text
    weatherPrediction = soup.find ("div", class_= "CurrentConditions--phraseValue--mZC_p").text
    
    locationLabel.config(text=location) # chúng ta đang đặt thuộc tính text của nhãn locationLabel thành giá trị của biến location.
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)
    
    temperatureLabel.after(60000,get_weather) #gọi là temperature sau 60000 ms của phương thức get_weather()
    window.update() #cập nhật lại cửa sổ làm việc window 




#Dưới đây là tạo gui trước và sau đó là áp dụng def get_weather đều có sự tính toán hết
locationLabel=Label(window,font=("Calibri Bold",20),bg="white") #tạo nhãn cho các biến 
locationLabel.grid(row=0,sticky="N", padx=100) #hiển thị text locationLabel
temperatureLabel= Label(window,font=("Calibri Bold",70),bg="white")#như trên# Font lớn nhất 
temperatureLabel.grid(row=1,sticky="W", padx=10)
weatherPredictionLabel=Label(window,font=("Calibri Bold",50),bg="white")# như trên#
weatherPredictionLabel.grid(row=2,sticky="W", padx=100)

get_weather() # tạo đối tượng sau khi tạo hàm phương thức
window.mainloop() #run the window
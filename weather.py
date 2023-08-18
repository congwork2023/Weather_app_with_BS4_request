import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image


url ="https://weather.com/en-CA/weather/today/l/c4877d013a65b996c469bc919c35c1b1af5cb13c0c6868275de92ba1e2a936cb7e6c9b3cf58bb491f3a1347e4d84b14e"
# Với cách này là lấy URL chưa phải là API

master=Tk() # tạo cửa sổ window
master.title("Weather App")
master.config(bg="white") #

img=Image.open("Img\weather_logo.png") #nằm trong module PIL có thể dùng thư mục thay toàn bộ đường dẫn dài
img=img.resize((150,150))# NẰM TRONG PIL -> thay đổi kích thước ảnh
img=ImageTk.PhotoImage(img) #add vào widget #có thể thay thế biến img bằng biến img2
Label(master, image=img, bg="white").grid(row=1,sticky="E") #######cái này để hiển thị logo image có thể thay thể biến image=img2

def getWeather():
    page = requests.get(url)
    soup =BeautifulSoup(page.content,"html.parser")
    
    location = soup.find ("h1",class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find ("span", class_ = "CurrentConditions--tempValue--MHmYY").text
    weatherPrediction = soup.find ("div", class_= "CurrentConditions--phraseValue--mZC_p").text

    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)
    
    temperatureLabel.after(60000,getWeather)
    master.update()
    
locationLabel = Label(master,font=("Calibri Bold",20),bg="white")
locationLabel.grid(row=0,sticky="N", padx=100)
temperatureLabel = Label(master,font=("Calibri Bold",70),bg="white")
temperatureLabel.grid(row=1,sticky="W", padx=40)
weatherPredictionLabel = Label(master,font=("Calibri bold", 51),bg="white")
weatherPredictionLabel.grid(row=2, sticky="W",padx=40)

getWeather()
master.mainloop()
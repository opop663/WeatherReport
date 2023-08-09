import requests
import config
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

API_KEY = config.api_key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
POLLUTION_URL = "http://api.openweathermap.org/data/2.5/air_pollution"

def callReport():
   try:
      city = locationVar.get()
      # request current weather data
      requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
      response = requests.get(requests_url)
      data = response.json()

      # save coordinate from current weather data
      lat = data["coord"]["lat"]
      lon = data["coord"]["lon"]

      # request pollution data using coordinate from current weather data
      requests_pollution = f"{POLLUTION_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
      pollution = requests.get(requests_pollution)
      pollutionData = pollution.json()
      
      # Report weather data
      weatherText.configure(text=data['weather'][0]["main"])
      tempText.configure(text=str(round(data["main"]["temp"] - 273.15, 2)) + " C")
      humidText.configure(text=str(data['main']['humidity']) + " %")
      windText.configure(text=str(data['wind']['speed']) + " m/sec")
      cloudText.configure(text=str(data['clouds']['all']) + " %")
      countryText.configure(text=data['sys']['country'])
      
      aqi = pollutionData["list"][0]["main"]["aqi"]
      if aqi == 1:
         aq = "Good"
      if aqi == 2:
         aq = "Fair"
      if aqi == 3:
         aq = "Moderate"
      if aqi == 4:
         aq = "Poor"
      if aqi == 5:
         aq = "Very Poor"  

      # Report pollution data
      qText.configure(text=aq)
      coText.configure(text=str(pollutionData["list"][0]['components']['co']) + " μg/m3")
      noText.configure(text=str(pollutionData["list"][0]['components']['no']) + " μg/m3")
      no2Text.configure(text=str(pollutionData["list"][0]['components']['no2']) + " μg/m3")
      o3Text.configure(text=str(pollutionData["list"][0]['components']['o3']) + " μg/m3")
      pm2_5Text.configure(text=str(pollutionData["list"][0]['components']['pm2_5']) + " μg/m3")
      nh3Text.configure(text=str(pollutionData["list"][0]['components']['nh3']) + " μg/m3")
      
   except:
      errorText.configure(text="Error. Please check your city name.", text_color='red')
      

# System Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App frame
app = ctk.CTk()
app.geometry("440x600")
app.title("Weather Report")
app.rowconfigure(3,weight=1)
app.rowconfigure(4, weight=1)
app.columnconfigure(0, weight=1)

# Title
title = ctk.CTkLabel(app, text="Weather Report", font=('Arial', 20, 'bold'))
title.grid(row=0, column=0,columnspan=2, padx=10, pady=10, sticky=tk.NSEW)

# InstuctionLabel
inputLabel = ctk.CTkLabel(app, text="Please input a city name")
inputLabel.grid(row=1, column=0, padx=10, pady=5, sticky=tk.NW)

# Location input
locationVar = tk.StringVar()
location = ctk.CTkEntry(app, width=250, height=40, textvariable=locationVar)
location.grid(row=2, column=0, padx=10, pady=10, sticky=tk.EW)

# Search Button
search = ctk.CTkButton(app, text="Search", height=40, command=callReport)
search.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

# Tabs
notebook = ttk.Notebook(app, width=400,height=360)
notebook.grid(row=3,columnspan=2, padx=10, pady=10, sticky=tk.EW)

# Frame1
frame1 = ttk.Frame(notebook, border=10, relief=tk.GROOVE)
frame1.columnconfigure(0,weight=1)
frame1.columnconfigure(1,weight=1)
frame1.rowconfigure(0)
frame1.grid(padx=10, pady=10, sticky=tk.EW)

# Frame2
frame2 = ttk.Frame(notebook, border=10, relief=tk.GROOVE)
frame2.columnconfigure(0, weight=1)
frame2.columnconfigure(1, weight=1)
frame2.rowconfigure(0)
frame2.grid(padx=10, pady=10, sticky=tk.EW)

## Current Weather 
# Weather
weatherLabel = ctk.CTkLabel(frame1, text="Weather: ")
weatherLabel.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
weatherText = ctk.CTkLabel(frame1, text="")
weatherText.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Temperature
tempLabel = ctk.CTkLabel(frame1, text="Temperature: ")
tempLabel.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
tempText = ctk.CTkLabel(frame1, text="C")
tempText.grid(row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Humidity
humidLabel = ctk.CTkLabel(frame1, text="Humidity: ")
humidLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)
humidText = ctk.CTkLabel(frame1, text="%")
humidText.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Wind Speed
windLabel = ctk.CTkLabel(frame1, text="Wind Speed: ")
windLabel.grid(row=3, column=0, padx=10, pady=10, sticky=tk.NSEW)
windText = ctk.CTkLabel(frame1, text="m/h")
windText.grid(row=3, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Cloud
cloudLabel = ctk.CTkLabel(frame1, text="Cloud: ")
cloudLabel.grid(row=4, column=0, padx=10, pady=10, sticky=tk.NSEW)
cloudText = ctk.CTkLabel(frame1, text="%")
cloudText.grid(row=4, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Country
countryLabel = ctk.CTkLabel(frame1, text="Country: ")
countryLabel.grid(row=5, column=0, padx=10, pady=10, sticky=tk.NSEW)
countryText = ctk.CTkLabel(frame1, text="")
countryText.grid(row=5, column=1, padx=10, pady=10, sticky=tk.NSEW)

## Pollution
# Overall Quality
qLabel = ctk.CTkLabel(frame2, text="Quality: ")
qLabel.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)
qText = ctk.CTkLabel(frame2, text="")
qText.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

# CO2
coLabel = ctk.CTkLabel(frame2, text="Carbon monoxide: ")
coLabel.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
coText = ctk.CTkLabel(frame2, text="μg/m3")
coText.grid(row=1, column=1, padx=10, pady=10, sticky=tk.NSEW)

# NO
noLabel = ctk.CTkLabel(frame2, text="Nitrogen monoxide: ")
noLabel.grid(row=2, column=0, padx=10, pady=10, sticky=tk.NSEW)
noText = ctk.CTkLabel(frame2, text="μg/m3")
noText.grid(row=2, column=1, padx=10, pady=10, sticky=tk.NSEW)

# NO2
no2Label = ctk.CTkLabel(frame2, text="Nitrogen dioxide: ")
no2Label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.NSEW)
no2Text = ctk.CTkLabel(frame2, text="μg/m3")
no2Text.grid(row=3, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Ozone
o3Label = ctk.CTkLabel(frame2, text="Ozone: ")
o3Label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.NSEW)
o3Text = ctk.CTkLabel(frame2, text="μg/m3")
o3Text.grid(row=4, column=1, padx=10, pady=10, sticky=tk.NSEW)

# PM 2.5
pm2_5Label = ctk.CTkLabel(frame2, text="PM 2.5: ")
pm2_5Label.grid(row=5, column=0, padx=10, pady=10, sticky=tk.NSEW)
pm2_5Text = ctk.CTkLabel(frame2, text="μg/m3")
pm2_5Text.grid(row=5, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Ammonia
nh3Label = ctk.CTkLabel(frame2, text="Ammonia: ")
nh3Label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.NSEW)
nh3Text = ctk.CTkLabel(frame2, text="μg/m3")
nh3Text.grid(row=6, column=1, padx=10, pady=10, sticky=tk.NSEW)

# ErrorText
errorText = ctk.CTkLabel(app, text="")
errorText.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky=tk.EW)

# add frame to tab
notebook.add(frame1, text="Current Weather")
notebook.add(frame2, text="Pollution")

# Run app
app.mainloop()

import requests
from tkinter import *
from tkinter import ttk

BG = '#364054'
# API and real time data collection
url = "https://foreca-weather.p.rapidapi.com/location/search/mumbai"

querystring = {"lang": "en", "country": "in"}

headers = {
    "X-RapidAPI-Key": "38e77c356dmshbab869e169aa0ffp16fc33jsn03b57eca2b5b",
    "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

# Creating the app
app = Tk()
# app.geometry('500x500')
app.config(
    background=BG
)
# Top Bar
title = Label(app, text='Weather App LSNX', font=('FreeSans', 20, 'bold'), bg=BG)
title.grid(row=0, column=0, padx=50, pady=5, columnspan=3)

input_label = Label(app, text="Enter city name", font=('Arial',15,'bold'), bg=BG)
input_label.grid(row=1, column=0, padx=1, pady=5)
input_box = Entry(app, font=('Arial',15,'normal'), bg=BG)
input_box.grid(row=1, column=1, padx=10)
line = ttk.Labelframe(app, text='Weather Information')
line.grid(row=2, padx=0, pady=10)

## Data Box
city_name = Label(line, text="City",bg=None)
city_name.grid(row=0, column=0,padx=10, pady= 5)
city_value = Label(line, text="Dhaka",bg=None)
city_value.grid(row=0, column=1,padx=10, pady= 5)

# Country data
country_name = Label(line, text="Country",bg=None)
country_name.grid(row=1, column=0,padx=10, pady= 5)
country_value = Label(line, text="Bangladesh",bg=None)
country_value.grid(row=1, column=1,padx=10, pady= 5)

input_btn = Button(app, text="Check", font=('Arial', 12, 'bold'), bg=BG)
input_btn.grid(row=1,column=2, padx=10)
app.mainloop()

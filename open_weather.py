import requests
from tkinter import *



def open_weather():
	city=city_listbox.get()
	url="https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
	res=requests.get(url)
	output=res.json()

	forecast=output['weather'][0]['description']
	temperature=output['main']['temp']
	pressure=output['main']['pressure']
	wind_speed=output['wind']['speed']

	forecast_label.configure(text="Forecast : "+ forecast)
	temperature_label.configure(text="Temperature : "+ str(temperature) + " Degrees Celsius")
	pressure_label.configure(text="Pressure : "+ str(pressure) + " Millibars")
	wind_speed_label.configure(text="Wind Speed  : "+ str(wind_speed) + " Kilometers Per Hour")
	


window=Tk()
window.geometry("500x500")

city_name_list=["New York","San Francisco","Chicago","Los Angeles"]

city_listbox=StringVar(window)
city_listbox.set("City Selector")
option=OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=2,column=2,padx=150,pady=10)

a=Button(window,text="Go!",width=15,command=open_weather)
a.grid(row=5,column=2,padx=150)


forecast_label=Label(window,font=("calibri",16,"bold"))
forecast_label.grid(row=10,column=2)


temperature_label=Label(window,font=("calibri",16,"bold"))
temperature_label.grid(row=12,column=2)


pressure_label=Label(window,font=("calibri",16,"bold"))
pressure_label.grid(row=14,column=2)

wind_speed_label=Label(window,font=("calibri",16,"bold"))
wind_speed_label.grid(row=16,column=2)

window.mainloop()
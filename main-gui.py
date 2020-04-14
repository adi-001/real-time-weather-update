import requests
import datetime
import tkinter

mainwindow = tkinter.Tk()
mainwindow.title("Weather API")
mainwindow.resizable(10,10)
mainwindow.configure(background='grey')


label = tkinter.Label(mainwindow, text="Enter City",background="orange",fg="Black")
label.grid(row=0, column=0,sticky= "NENSSESW")

cityValue = tkinter.StringVar()
e = tkinter.Entry(mainwindow,textvariable=cityValue)
e.grid(row=0, column=1,sticky= "NENSSESW")



button = tkinter.Button(mainwindow, text="Submit",background="Black",fg="White", command=lambda: weather_data())
button.grid(row=1, column=0, columnspan=2,sticky= "NENSSESW")

datalabel= tkinter.Label(mainwindow)
datalabel.grid(row=2, column=0,sticky= "NENSSESW",columnspan=2)






def weather_data():
    city = str(e.get())
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url = url + cityValue.get()
    print(new_url)

    data = requests.get(new_url).json()
    print(data)

    if(data['cod']=='404'or data['cod']=='400'):
        print('City Not Found')
        datalabel.configure(text='City Not Found')
        return

    longitude = data["coord"]["lon"]
    latitude = data["coord"]["lat"]

    wind_speed = data["wind"]["speed"]

    sunrise_timestamp = data["sys"]["sunrise"]
    sunrise_time = time_stamp(sunrise_timestamp)

    sunset_timestamp = data["sys"]["sunset"]
    sunset_time = time_stamp(sunset_timestamp)

    pressure = data["main"]["pressure"]
    date = data["dt"]
    date_updated = time_stamp(date)

    text = '''
    weather Report                                 :{1}
    Latitude                                       :{2}
    longitude                                      :{3}
    Windspeed                                      :{4}
    SunRise                                        :{5}
    SunSet                                         :{6}
    Date                                           :{7}
    Pressure                                       :{8}
    '''.format(city, test(), latitude, longitude, wind_speed, sunrise_time, sunset_time, date_updated, pressure)
    datalabel.configure(text = text)
    return text



def test():
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url = url + "India"
    data = requests.get(new_url).json()
    for x in data["weather"]:
        description = x["description"]
        main = x["main"]
    return main + description



def time_stamp(number):
    date_time = datetime.datetime.fromtimestamp(int(number)).strftime('%Y-%m-%d %H:%M:%S')
    return date_time




mainwindow.mainloop()

# Python program to find current weather details of any city  using openweathermap api 

# import required modules
try:
	import sys
	import requests, json 
	from time import sleep
	from urllib.parse import urlencode
	from urllib.request import urlretrieve
	from PIL import Image
except Exception as e:
	print("Some modules are missing : {}".format(e))

def anim_text(anim_string):
  for word in anim_string:
    print(word, end = "")
    sys.stdout.flush()
    sleep(0.05)
  print("")
  
# Enter your API key here 
api_key = "c41af2fc52b7d4c77ffb1848c470bc0d"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ") 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url)

x = response.json()
#anim_text(x)
y = dict()

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = round(y["temp"] - 273,2)

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	anim_text("\tTemperature = {} C".format(current_temperature) +
              "\n\tatmospheric pressure = {} hpa".format(current_pressure) +
	      "\n\thumidity = {} %".format(current_humidiy) +
              "\n\tdescription = {} ".format(weather_description))
else:
        anim_text(" City Not Found ")

query = str(input('Wanna check for redundancy?\t'))
if query =='Y':
        anim_text('Checking for redundancy in ')
        params = urlencode(dict(access_key="0970cc78d7be45dbb83cca8b6086032d",url="https://www.google.com/search?q=temperature+in+{}+in+celsius".format(city_name)))
        urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshot.jpeg")

        # Screenshot image being Displayed
        img = Image.open("screenshot.jpeg")
        left = 90
        right = 900
        top = 150
        bottom = 800
        im = img.crop((left,top,right,bottom))
        im.show()

                 

                                                                                                                


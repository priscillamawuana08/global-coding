import pyowm
 
owm = pyowm.OWM('276ccab4f995cf92e4df82e6c6fcaf83')
observation = owm.weather_at_place('Ghana,koforidua')
w = observation.get_weather()
 
w.get_wind()
w.get_humidity()


print(w.get_wind())
print(w.get_humidity())


from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
@csrf_exempt
def main(request):
	if request.method == "POST":
		search_address = request.POST["location"]
		url_temp = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str(search_address) + '&key=AIzaSyCj8BjyPXjn8GooYyfAk2uVStS0B0oCwQA'
		temp = requests.get(url_temp).json()
		latitude = temp['results'][0]['geometry']['bounds']['southwest']['lat']
		longitude = temp['results'][0]['geometry']['bounds']['southwest']['lng']
		address = temp['results'][0]['formatted_address']
		url = 'http://api.openweathermap.org/data/2.5/weather?lat=' +str(latitude) +'&lon='+str(longitude)+'&APPID=926c62271d95893e58662045b0dc0ea4&units=metric'
		data = requests.get(url)
		data = data.json()
		return render(request, 'weather/index.html',
						  { 'data' : data ,'latitude': latitude, 'longitude': longitude, 'address': address})
	else:
		return render(request, 'weather/index.html')
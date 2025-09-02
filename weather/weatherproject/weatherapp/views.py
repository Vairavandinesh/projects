from django.shortcuts import render
import requests
def home(request):
    weather_data=None
    if 'city' in request.GET:
        city=request.GET['city']
        api_key='3119396ad3a80502dc742b23c3c61524'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response=requests.get(url).json()
        if response.get('main'):
            weather_data={
                'city':city,
                'temperature':response['main']['temp'],
                'description':response['weather'][0]['description'],
                'humidity':response['main']['humidity']
            }
    return render(request,'weather app/home.html',{'weather':weather_data})
# Create your views here.

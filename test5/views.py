from django.shortcuts import render
import json
import urllib.request
import json
# Create your views here.
def home(request):
    if request.method == 'POST':
        # Get the city name from the user api = http://api.openweathermap.org/data/2.5/weather
        city = request.POST.get('city', 'True')
        # retreive the information using api
        source = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5d1c7619508328fdc42c85ad361f602f').read()
        # convert json data file into python dictionary
        list_of_data = json.loads(source)
        # create dictionary and convert value in string
        context = {
            'city': city,
            "country_code": str(list_of_data['sys']['country']),
            "count_code": str(list_of_data['cod']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "temp_new": int(list_of_data['main']['temp']),
        }
    else:
        context = {}
    return render(request, 'test5/home.html', context)

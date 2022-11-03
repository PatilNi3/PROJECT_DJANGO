from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']

    #retreive the information using api
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&units=imperial&appid=79f6163d4e46d752483a7e65750359c2').read()

    # convert json data file into python directory
        list_of_data = json.loads(source)

    # create dictionary and convert value instring
        context = {'city':city,
               "country_code":str(list_of_data['sys']['country']),
               "coordinate":str(list_of_data['coord']['lon'])+''+str(list_of_data['coord']['lat']),
               "temp":str(list_of_data['main']['temp']) + 'k',
               "pressure":str(list_of_data['main']['pressure']),
               "humidity":str(list_of_data['main']['humidity'])}
    else:
        context={}
    return render(request, 'Weather.html', context)


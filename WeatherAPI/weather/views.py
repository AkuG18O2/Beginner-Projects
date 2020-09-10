from django.shortcuts import render 
import json 
import urllib.request 
    
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
    
        source = urllib.request.urlopen( 
            'https://api.weatherapi.com/v1/current.json?key=5ffff6aed6794d55ab1101424201009&q=' + city).read() 
  
        sourcedata = json.loads(source) 
  
        data = { 
            "location": str(sourcedata['location']['region']), 
            "coordinates": str(sourcedata['location']['lat']) + ', '
                        + str(sourcedata['location']['lon']), 
            "temperature": str(sourcedata['current']['temp_c']) + ' C', 
            "condition": str(sourcedata['current']['condition']['text']), 
            "humidity": str(sourcedata['current']['humidity']),
            "wind": str(sourcedata['current']['wind_kph']) + ' kph',
            "pressure": str(sourcedata['current']['pressure_mb']) + ' mbar',
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "weather/index.html", data)
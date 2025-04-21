from django.shortcuts import render
from .models import Projects, Api
from django.http import JsonResponse


def home(request):
    all_data = Projects.objects.order_by('-ts')[:100]
    api_data = Api.objects.order_by('-ts')[:100]
    latest = all_data[0]
    latest_api = api_data[0]

    timestamps = [entry.ts.strftime("%Y-%m-%d %H:%M") for entry in reversed(all_data)]
    pm_values = [entry.pm2_5 for entry in reversed(all_data)]
    pm10_values = [entry.pm10 for entry in reversed(all_data)]
    humidity_values = [entry.humidity for entry in reversed(all_data)]
    temperature_values = [entry.temp for entry in reversed(all_data)]
    wind_speed_values = [entry.wind_speed for entry in reversed(api_data)]
 
    

    return render(request, 'home.html', {
        'latest': latest,
        'timestamps': timestamps,
        'pm_values': pm_values,
        'pm10_values': pm10_values,
        'humidity_values': humidity_values,
        'temperature_values': temperature_values,
        'wind_speed_values': wind_speed_values,
        'latest_wind': latest_api.wind_speed,
        
    })



def api_data(request):
    api_data = Api.objects.order_by('-ts')[:100]
    latest_api = api_data[0]

    data = {
        'timestamps': [entry.ts.strftime("%Y-%m-%d %H:%M") for entry in reversed(api_data)],
        'wind_speed_values': [entry.wind_speed for entry in reversed(api_data)],
        'latest_wind': latest_api.wind_speed,
    }
    return JsonResponse(data)

def average_data(request):
    all_data = Projects.objects.all()
    total_pm2_5 = sum(entry.pm2_5 for entry in all_data)
    total_pm10 = sum(entry.pm10 for entry in all_data)
    total_humidity = sum(entry.humidity for entry in all_data)
    total_temp = sum(entry.temp for entry in all_data)
    count = len(all_data)

    average_pm2_5 = total_pm2_5 / count if count > 0 else 0
    average_pm10 = total_pm10 / count if count > 0 else 0
    average_humidity = total_humidity / count if count > 0 else 0
    average_temp = total_temp / count if count > 0 else 0

    return render(request, 'average_data.html', {
        'average_pm2_5': average_pm2_5,
        'average_pm10': average_pm10,
        'average_humidity': average_humidity,
        'average_temp': average_temp,
    })
    

def statistics(request):
    return render(request, 'statistics.html') 
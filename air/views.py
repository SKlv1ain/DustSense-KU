from django.shortcuts import render
from .models import Projects

def home(request):
    all_data = Projects.objects.order_by('-ts')[:20]
    latest = all_data[0]

    timestamps = [entry.ts.strftime("%Y-%m-%d %H:%M") for entry in reversed(all_data)]
    pm_values = [entry.pm2_5 for entry in reversed(all_data)]
    pm10_values = [entry.pm10 for entry in reversed(all_data)]
    humidity_values = [entry.humidity for entry in reversed(all_data)]
    temperature_values = [entry.temp for entry in reversed(all_data)]

    return render(request, 'home.html', {
        'latest': latest,
        'timestamps': timestamps,
        'pm_values': pm_values,
        'pm10_values': pm10_values,
        'humidity_values': humidity_values,
        'temperature_values': temperature_values
    })
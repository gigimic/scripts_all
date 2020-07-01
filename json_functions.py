
import json

# Reading JSON with the loads() Function
# loads is load string 
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

# Writing JSON with the dumps() Function
# dumps is dump string 
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)

# Collect weather data: automation

import json, requests, sys
APPID = 'name of YOUR_APPID'

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: filename.py city_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url ='https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APPID)
response = requests.get(url)
response.raise_for_status()

#print(response.text) 
# The response.text member variable holds a large string of JSON-formatted data.
# 
#    
# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
# The following commands neatly print the weather data.

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
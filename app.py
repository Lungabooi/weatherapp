import requests
# creating a viriable for api key
api_key = 'ebbfc86a6aa7d61ddf094e7df2e69d83'

# Asking user to enter city and print the user input 
user_input = input("Enter city :  ")
print(user_input)

# 
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print('Location can not be found')
else:
 weather = (weather_data.json())['weather'][0]['main']
 temp = round(weather_data.json()['main']['temp'])

 print(f'The weather in {user_input} is : {weather}')
 print(f'The temp in {user_input} is: {temp} °C')
    


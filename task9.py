import requests

WEATHER_API_KEY = '8c2ae2725a5727448f1b874e3c7292fa'  # replace with your actual API key

def gather_weather_info(task_type):
    location = input("Please enter the location: ")

    if task_type == 'current':
        return get_current_weather(location)
    elif task_type == 'history':
        date = input("Please enter the date (YYYY-MM-DD): ")
        return get_weather_history(location, date)
    elif task_type == 'forecast':
        return get_weather_forecast(location)
    else:
        return "Invalid task type."

def get_current_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

def get_weather_history(location, date):
    # Convert date to a Unix timestamp (assuming the API requires it)
    from datetime import datetime
    timestamp = int(datetime.strptime(date, '%Y-%m-%d').timestamp())
    
    # You would normally need to get the latitude and longitude of the location
    # For simplicity, we'll assume these are provided directly (or you'd need an additional API call)
    lat = 0.0  # replace with actual latitude
    lon = 0.0  # replace with actual longitude

    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={timestamp}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

def get_weather_forecast(location):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={WEATHER_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.json().get('message', '')}"

def main():
    print("Welcome to the AI Task Execution System!")
    task = input("What task would you like to perform? (e.g., 'current weather', 'weather history', 'weather forecast'): ")

    if 'current weather' in task.lower():
        result = gather_weather_info('current')
    elif 'weather history' in task.lower():
        result = gather_weather_info('history')
    elif 'weather forecast' in task.lower():
        result = gather_weather_info('forecast')
    else:
        result = "Task not recognized. Please specify a valid task like 'current weather', 'weather history', or 'weather forecast'."

    print("Result:", result)

if __name__ == '__main__':
    main()

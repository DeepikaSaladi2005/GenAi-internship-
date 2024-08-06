import requests
from langgraph import Graph, tool

# Replace with your actual API key
API_KEY = "8c2ae2725a5727448f1b874e3c7292fa"

# Define a custom tool to get weather data
@tool
def get_weather(city: str) -> str:
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The weather in {city} is currently {weather_description} with a temperature of {temperature}°C."
    else:
        return f"Could not retrieve weather data for {city}. Please check the city name and try again."

# Create a graph and register the custom tool
graph = Graph()
graph.add_tool(get_weather)

# Example usage
def main():
    city_name = "Mumbai"
    weather_info = graph.run("get_weather", city=city_name)
    print(weather_info)

if __name__ == "__main__":
    main()


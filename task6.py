import os
import requests
import openai
from crewai import Agent, Task, Crew, Process
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import gradio as gr

# Hardcode your API keys here
OPENAI_API_KEY = "APIKey"
WEATHER_API_KEY = "WeatherApikey"



# 1. Configuration and Tools
llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

class WeatherAPITool:
    @tool("Weather Fetcher")
    def fetch_weather(location: str):
        """Fetch current weather information for a given location."""
        try:
            # Define the endpoint and parameters
            url = "http://api.weatherapi.com/v1/current.json"
            params = {
                "key": WEATHER_API_KEY,
                "q": location,
                "aqi": "no"  # Don't fetch air quality index data
            }
            
            # Make the request to the WeatherAPI
            response = requests.get(url, params=params)
            
            # Check if the response was successful
            if response.status_code == 200:
                weather_data = response.json()
                location_name = weather_data['location']['name']
                temp_c = weather_data['current']['temp_c']
                condition = weather_data['current']['condition']['text']
                return f"The current weather in {location_name} is {temp_c}°C with {condition}."
            else:
                return f"Failed to fetch weather data. Status code: {response.status_code}"
        
        except Exception as error:
            print("Error while fetching weather data:", error)
            return str(error)

# 2. Creating an Agent for Weather Tasks
weather_agent = Agent(
    role='Weather Analyst',
    goal='Provide accurate and up-to-date weather information for any location',
    backstory='Expert in meteorology and weather data analysis.',
    tools=[WeatherAPITool.fetch_weather],
    verbose=True,
    llm=llm
)

# 3. Defining a Task for Weather Data Fetching
weather_task = Task(
    description='This will be replaced by user prompt',
    expected_output='Fetch current weather information using the Weather Fetcher tool',
    agent=weather_agent,
    tools=[WeatherAPITool.fetch_weather]
)

# 4. Creating a Crew with Weather Focus
weather_crew = Crew(
    agents=[weather_agent],
    tasks=[weather_task],
    process=Process.sequential,
    manager_llm=llm
)

# 5. Define Weather Interface Function
def weather_interface(location):
    weather_task.description = f"Fetch weather for {location}"
    result = weather_crew.kickoff()
    
    # Log and print detailed usage information
    if 'usage' in result:
        token_usage = result['usage']['total_tokens']
        print(f"Tokens used: {token_usage}")
    else:
        print("Token usage data is not available.")

    return result

# 6. Define and Launch Gradio Interface
iface = gr.Interface(
    fn=weather_interface,
    inputs=gr.Textbox(lines=1, placeholder="Enter location (e.g., New York)"),
    outputs="text",
    title="Weather Fetcher",
    description="Get current weather information for any location using the WeatherAPI."
)

iface.launch()

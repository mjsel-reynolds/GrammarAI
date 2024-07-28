import openai
from openai import OpenAI
from geopy import Nominatim
import requests
import json
from dotenv import load_dotenv
import config

# Connect to Veg Grow+ OpenAI Assistant
load_dotenv()
client = OpenAI(api_key=config.api_key)
assistant_id = 'asst_PdQ4sX2gOIedrOdjdx9Pek4Z'


def get_weather(area):
    # Get lat / lon of location from user
    geolocator = Nominatim(user_agent='myapplication')
    location = geolocator.geocode(str(area))

    # Access OpenWeatherAPI for daily weather forecast of given area
    access_key = 'f778df8bf125a8d5dd4d74a062abf8c4'
    weather_url = 'https://api.openweathermap.org/data/3.0/onecall?lat='+str(location.latitude)+'&lon='+\
                  str(location.longitude)+'&exclude=hourly&appid=' + access_key

    # Get the response from fetched url
    response = requests.get(weather_url)
    weather_info = response.json()

    # Main description of Rain that Day
    daily_weather = weather_info['daily'][2]['weather'][0]['description']
    daily_rain = weather_info['daily'][2]['rain']

    return f"""Based on your given location: {area} \n
        ~ The forecasted weather for today is: {daily_weather} \n
        ~ The total rainfall for today is: {daily_rain} \n
    """


# Open AI Veg Grow+ Assistant
thread = client.beta.threads.create()


while True:
    user_input = input('User :')
    message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = 'user',
        content = user_input,
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id='asst_PdQ4sX2gOIedrOdjdx9Pek4Z',
    )
    #if run.status == 'completed':
        #messages = client.beta.threads.messages.list(
            #thread_id=thread.id
        #)
        #print('Veg Grow+:' + messages.data[0].content[0].text.value)

    tool_outputs = []

    if run.status == 'requires_action':
        for tool in run.required_action.submit_tool_outputs.tool_calls:
            if tool.function.name == 'get_weather':
                arg = json.loads(tool.function.arguments)['location']
                res = get_weather(arg)

                tool_outputs.append({
                    'tool_call_id': tool.id,
                    'output': str(res)
                })
    if tool_outputs:
        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        print('Veg Grow+:' + messages.data[0].content[0].text.value)

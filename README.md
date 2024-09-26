# Veg_Grow+
(FOR MEGAHACKS 2024 HACKATHON) 
a custom OpenAI Assistant to give you custom plant care guides based on the weather in your current location
e.g. can tell you whether you should water your plants that day based on the weather in your city

In-Depth:
The main purpose of this project is to create a user-friendly AI for students to learn more about agriculture, cosmetology, and plant life. Veg_Grow+ utilizes function calling and file retrieval to answer questions about different types of plants and how to care for them based on the weather in a given location. It advises others to thoughtfully care for plants based on the environment and their specific needs. The AI uses gets information from Purdue agricultural reports on various vegetable and fruit plants. I also gave my Veg_Grow Assistant access to a weather_api to get the daily forecast weather for a given location.

Inspiration:
A lot of plants (especially in Florida) rot out because they are over-watered or out in the sun too long. Veg_Grow+ aims to remedy that. Students could use Veg_Grow to find the relationship between the current weather and plant growth. In areas like Florida where rainfall is frequent and the weather changes sporadically, students could use this AI to learn new gardening habits. Likewise, biology teachers could use this tool to better guide their students during experiments, such as when to water their plants (or do other care activities) depending on where they live and the weather forecast for that day.

APIs / External Modules Used:
- OpenAI Assistant
- OpenWeatherMap API
- Gradio
- Geopy

Additional Sources:
- https://platform.openai.com/docs/quickstart
- https://openweathermap.org/api/one-call-3#history
- https://www.jimmymills.io/blog/openai-assistants-api/retrieval

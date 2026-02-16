# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY* : CODTECH IT SOLUTION

*NAME* : DEEPAK T

*INTERN ID* :CTIS5745

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 8 WEEKS

*MENTOR* : NEELA SANTHOSH

1.PROJECT OVERVIEW :
This Python file is designed to create a Global Weather Analysis Dashboard. It collects real-time weather information from the OpenWeatherMap API for multiple cities and then visualizes the results using bar charts. The final output is displayed as a dashboard.

2.LIBRARIES :
1.Requests Library -The requests library is used to send HTTP requests to the OpenWeatherMap API. It helps the program connect to the internet and fetch live weather data.
2.Matplotlib Library -Matplotlib is used for plotting graphs. It is responsible for creating the figure, subplots, titles, saving the image, and showing the output.
*plt.subplots()
*plt.suptitle()
*plt.tight_layout()
*plt.savefig()
*plt.show()
3.Pandas Library  -Pandas is used to store the weather data in a structured table format called a DataFrame. This makes it easy to manage and plot the data.
4.Seaborn Library -Seaborn is used to create attractive and easy-to-read visualizations. In this file, it is mainly used to create bar charts for temperature and humidity.

3.KEY VARIABLES :
#API Key -The API key is required to access OpenWeatherMap services.

#City List
The program collects weather details for these cities:
CITIES = ['New York', 'London', 'Mumbai', 'Tokyo', 'Sydney', 'Paris', 'Dubai']

#Base URL
This is the API endpoint used for fetching weather data.
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

FUNCTIONS :
1.Fetching Weather Data -Temperature (°C),Humidity,Condition.
2.Creating the Dashboard :
                         *Temperature Comparison
                         *Humidity Comparison
FINAL OUTPUT :
This Python file uses the OpenWeatherMap API to fetch live weather data for multiple cities and creates a dashboard using Seaborn and Matplotlib bar charts.
<img width="1600" height="600" alt="Image" src="https://github.com/user-attachments/assets/b8c24809-405e-4c68-aff4-2d1520112c2f" />

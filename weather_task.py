import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

API_KEY = '2037063ab7d8168386aaca53bc1c1a96'
CITIES = ['New York', 'London', 'Mumbai', 'Tokyo', 'Sydney', 'Paris', 'Dubai']
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_dashboard_data(cities):
    weather_list = []
    for city in cities:
        params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            weather_list.append({
                'City': city,
                'Temperature (°C)': data['main']['temp'],
                'Humidity (%)': data['main']['humidity'],
                'Condition': data['weather'][0]['description'].capitalize()
            })
    return pd.DataFrame(weather_list)

def create_dashboard(df):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    sns.set_theme(style="whitegrid")

    # Plot 1: Temperature Comparison
    sns.barplot(ax=axes[0], x='City', y='Temperature (°C)', data=df, palette='Oranges_d')
    axes[0].set_title('City Temperatures (°C)', fontsize=14, fontweight='bold')
    axes[0].tick_params(axis='x', rotation=45)

    # Plot 2: Humidity Comparison
    sns.barplot(ax=axes[1], x='City', y='Humidity (%)', data=df, palette='Blues_d')
    axes[1].set_title('City Humidity Levels (%)', fontsize=14, fontweight='bold')
    axes[1].tick_params(axis='x', rotation=45)

    plt.suptitle('Global Weather Analysis Dashboard', fontsize=20, y=1.05)
    plt.tight_layout()
    
    plt.savefig('weather_dashboard.png')
    plt.show()

if __name__ == "__main__":
    print("Connecting to OpenWeatherMap API...")
    df = fetch_weather_dashboard_data(CITIES)
    
    if not df.empty:
        print("\nFetched Data Summary:")
        print(df[['City', 'Temperature (°C)', 'Humidity (%)', 'Condition']])
        create_dashboard(df)
    else:
        print("Error: Could not fetch data. Check your API key!")
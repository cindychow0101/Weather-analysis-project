import requests
import pandas as pd
import schedule
import time
import csv
from datetime import datetime
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
def weather_data():
    target_city = ['Hong Kong', 'Japan', 'Seoul']
    for city in target_city:
        API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'sea_level': data['main'].get('sea_level', None),  # Handle case if sea level data is not available
                'visibility': data['visibility'],
            }
            print(weather_data)
            insert_weather_data(weather_data)

def create_table():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_info (
        city VARCHAR(20) NOT NULL,
        timestamp VARCHAR(20) NOT NULL,
        temperature FLOAT NOT NULL,
        humidity INT NOT NULL,
        sea_level INT,
        visibility INT NOT NULL
    )
    ''') 
    conn.commit()
    conn.close()

def insert_weather_data(data):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO weather_info (city, timestamp, temperature, humidity, sea_level, visibility)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (data['city'], data['timestamp'], data['temperature'], data['humidity'], data['sea_level'], data['visibility']))
    conn.commit()
    conn.close()

def export_to_csv():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {'weather_info'}')
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    with open('weather_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)
    conn.close()
    print(f"Data exported to {'weather_data.csv'} successfully.")

def weather_by_city():
    df_weather = pd.read_csv('weather_data.csv')
    unique_city = df_weather['city'].unique()
    for city in unique_city:
        city_df = df_weather[df_weather['city'] == city]
        city_df.to_csv(f'{city}.csv', index=False)

def main():
    create_table()
    interval = input("Enter the interval in minutes (default is 1): ")
    interval = int(interval) if interval.isdigit() else 1

    schedule.every(interval).minutes.do(weather_data)
    
    print(f"Scheduler started. Fetching weather data every {interval} minute(s).")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
if __name__ == "__main__":
    main()

#export_to_csv()
#weather_by_city()
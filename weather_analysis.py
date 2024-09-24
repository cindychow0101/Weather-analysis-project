import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

data = pd.read_csv('weather_data.csv')
data['timestamp'] = pd.to_datetime(data['timestamp'])
data_grouped = data[['city','temperature','humidity','sea_level','visibility']]

def view_weather_data():
    while True:
        print("\nWhich city weather data do you want to view?:")
        print("1. Hong Kong")
        print("2. Japan")
        print("3. Seoul")
        print("4. None (Back to main menu)")

        choice = input("Choose an option: ")

        city_mapping = {
            '1': 'Hong Kong',
            '2': 'Japan',
            '3': 'Seoul'
        }

        if choice in city_mapping:
            city = city_mapping[choice]
            conn = sqlite3.connect('weather.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM weather_info WHERE city = ?', (city,))
            rows = cursor.fetchall()
            conn.close()

            for row in rows:
                print(f"city: {row[0]}, timestamp: {row[1]}, temperature: {row[2]}, humidity: {row[3]}, sea_level: {row[4]}, visibility: {row[5]}")
        
        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

def view_table():
    while True:
        print("\nWhich table do you want to view?:")
        print("1. Mean table")
        print("2. Max table")
        print("3. Min table")
        print("4. None (Back to main menu)")

        choice = input("Choose an option: ")

        if choice == '1':
            city_mean()
        elif choice == '2':
            city_max()
        elif choice == '3':
            city_min()
        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

def city_mean():
    data_mean = data_grouped.groupby('city').mean()
    print("Mean weather data by city:")
    print(data_mean)

def city_max():
    data_max = data_grouped.groupby('city').max()
    print("Max weather data by city:")
    print(data_max)

def city_min():
    data_min = data_grouped.groupby('city').min()
    print("Min weather data by city:")
    print(data_min)

def temp_graph():
    plt.figure(figsize=(12, 6))
    for city in data['city'].unique():
        city_data = data[data['city'] == city]
        plt.plot(city_data['timestamp'], city_data['temperature'], marker='o', label=city)
    plt.title('Temperature Trends by City')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.legend(title='City')
    plt.tight_layout()
    plt.show()

def humi_graph():
    plt.figure(figsize=(12, 6))
    for city in data['city'].unique():
        city_data = data[data['city'] == city]
        plt.plot(city_data['timestamp'], city_data['humidity'], marker='o', label=city)
    plt.title('Humidity Trends by City')
    plt.xlabel('Time')
    plt.ylabel('Humidity (%)')
    plt.legend(title='City')
    plt.tight_layout()
    plt.show()

def sea_graph():
    plt.figure(figsize=(12, 6))
    for city in data['city'].unique():
        city_data = data[data['city'] == city]
        plt.plot(city_data['timestamp'], city_data['sea_level'], marker='o', label=city)
    plt.title('Sea Level Pressure Trends by City')
    plt.xlabel('Time')
    plt.ylabel('Sea Level Pressure (hPa)')
    plt.legend(title='City')
    plt.tight_layout()
    plt.show()

def GUI_graph():
    def execute_choice():
        selected_choice = choice.get()
        if selected_choice == "1. Temperature":
            temp_graph()
        elif selected_choice == "2. Humidity":
            humi_graph()
        elif selected_choice == "3. Sea Level Pressure":
            sea_graph()

    root = tk.Tk()
    root.title("Weather Data")
    root.geometry("400x300")
    root.configure(bg="#e0f7fa")

    title_label = tk.Label(root, text="Weather Graph Viewer", font=("Helvetica", 16, "bold"), bg="#e0f7fa")
    title_label.pack(pady=10)

    question_label = tk.Label(root, text="Which graph do you want to view?", font=("Helvetica", 12), bg="#e0f7fa")
    question_label.pack(pady=10)

    options = [ 
        "1. Temperature", 
        "2. Humidity", 
        "3. Sea Level Pressure"
    ] 

    choice = StringVar()
    choice.set(options[0])  # Set default value
    drop = OptionMenu(root, choice, *options)
    drop.config(font=("Helvetica", 12))
    drop.pack(pady=10)

    confirm_button = tk.Button(root, text="Confirm", command=execute_choice, font=("Helvetica", 12), bg="#4db6e1", fg="black")
    confirm_button.pack(pady=20)

    back_label = tk.Label(root, text="(You may return to the main menu by closing this window.)", font=("Helvetica", 12), bg="#e0f7fa")
    back_label.pack(pady=10)

    root.mainloop()

def main():
    while True:
        print("\nWelcome! You can view the weather data of Hong Kong, Japan, Seoul here.")
        print("Main menu:")
        print("1. View weather data of city")
        print("2. View graph and compare by city")
        print("3. View table and compare by city")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_weather_data()
        elif choice == '2':
            GUI_graph()
        elif choice == '3':
            view_table()
        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
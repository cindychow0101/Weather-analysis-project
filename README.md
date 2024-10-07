# Weather Analysis Project

## Overview

This project collects, stores, and analyzes weather data from various cities using the OpenWeatherMap API. It allows users to get current weather information, save it in a SQLite database, and display the data with graphs. There is also a user-friendly interface to choose the graphs users want to see.

## Features

- **Data Retrieval**: Fetches current weather data for specified cities (Hong Kong, Japan, Seoul) using OpenWeatherMap API.
- **Data Storage**: Saves weather data into a SQLite database.
- **Data Export**: Exports collected data to a CSV file for further analysis.
- **Data Visualization**: Provides various visualizations (temperature, humidity, sea level pressure) through graphs using Matplotlib.
- **User Interface**: A basic GUI for selecting which graph to display.

## Usage

### Data Collection

- Upon running the data collector script, you will be prompted to enter the interval (in minutes) for fetching weather data. The default is 1 minute.
- The weather data will be printed to the console and stored in the SQLite database.

### Data Visualization

- The visualizer script provides a menu to:
  - View weather data for specific cities.
  - View graphical representations of temperature, humidity, and sea level pressure.
  - View statistical summaries (mean, max, min) of the weather data.

  ![Main](/images/main%20menu.png){width=250}
  ![GUI](/images/GUI.png){width=250}

### Menu Options

- **Weather Data Viewing**: Choose a city to view its weather data.
- **Graphical Analysis**: Select which type of graph to display.
- **Statistical Analysis**: View mean, max, or min values for the weather data.

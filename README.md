```markdown
# Weather CLI App

This is a simple command-line interface (CLI) application that fetches and displays the current weather information for a specified city using the OpenWeatherMap API.

## Features

- Fetches current weather information for a city.
- Displays temperature, humidity, pressure, weather description, and wind speed.
- Supports command-line arguments for specifying the city.

## Requirements

- Python 3.x
- `requests` library (can be installed via pip)

## Installation

1. **Clone the repository:**

```sh
git clone https://github.com/AustinKinOry/python-weather-cli-app.git
cd python-weather-cli-app
```

2. **Install the required packages:**

```sh
pip install requests
```

3. **Get an API key:**

   Sign up for an API key from [OpenWeatherMap](https://openweathermap.org/api).

## Usage

1. **Update the script with your API key:**

   Open the `weather_cli.py` file and replace `'your_api_key_here'` with your actual API key.

```python
API_KEY = 'your_api_key_here'
```

2. **Run the script:**

```sh
python weather_cli.py "City_Name"
```

For example:

```sh
python weather_cli.py "Nairobi"
```

## Example Output

```
Enter city name: Nairobi
City: Nairobi
Temperature: 25°C
Humidity: 60%
Pressure: 1012 hPa
Weather: clear sky
Wind Speed: 3.6 m/s
```

## Improvements

You can further improve this CLI app by:

- Adding error handling for network issues.
- Supporting different units (metric, imperial).
- Adding more command-line arguments for additional options.
- Displaying more detailed weather information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


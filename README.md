# Tempbot 2
This Telegram bot tells the temperatures of 1-Wire sensors (DS18B20) connected to a Raspberry Pi.

## Installation

### Set up 1-Wire
First it is needed to set up the 1-Wire system. Follow [this guide](https://tutorials-raspberrypi.com/raspberry-pi-temperature-sensor-1wire-ds18b20/) for details.

### Clone project
Clone this project to a Raspberry Pi (for example the user's home directory):
```
git clone https://github.com/samporapeli/tempbot-2.git
```

### Set up project
Change to the project folder:
```
cd tembot-2
```
Set up virtualenv (run `sudo apt install virtualenv` if not already installed) and install requirements:
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
```

### Telegram bot token
Use [@Botfather](https://t.me/BotFather) to create a bot and receive authorization token. Place the token to `token.txt` file in project root directory.

## Usage
Use `./start.sh` in project root directory to start the Telegram bot and temperature reader. 

## Configuration
There's a configuration file, `config.py`, that can be used for naming the sensors and other preferences. 

Naming of sensors is done by modifying the python dictionary `sensor_names`, which has by default IDs and Finnish names of my system's few temperature sensors. Since they aren't relevant in any other system, they can and should be replaced by relevant key-value pairs. It might be helpful to run `python3 sensor_test.py`, where sensor names and temperatures can be seen. Temperatures update every five seconds, so it's easy to find right sensor ID when e. g. heating one sensor up. Exit with Ctrl-C.

If installation system has different path for 1-Wire sensors, it can be configured from onewire_path.

If point is preferred over comma in decimal numbers, change `use_decimal_comma` to `False`.

"""
Config Reader

A simple script for reading key-value pairs from a configuration file.

Input Requirements:
- The input should be the name of the configuration file to be read (e.g., 'setting2.cfg').
- The configuration file should contain sections, each containing key-value pairs.

Output Values:
- The values of the keys in the specified sections of the configuration file.

Example of Usage:
import config_reader

config_data = config_reader.read_config('setting2.cfg')

print("Person's name:", config_data['Person']['name'])
print("Person's age:", config_data['Person'].getint('age'))
print("Person's middle name:", config_data.get('Person', 'middle_name', fallback='I don't have a middle name'))

for key in config_data['DEFAULT']:
print(key, '=', config_data['DEFAULT'][key])


"""

import configparser

def read_config(file_name):
    config = configparser.ConfigParser()
    config.read(file_name)    
    return config


#Example of Usage:
config_data = read_config('setting2.cfg')
print(f"Config data: {config_data.items()}")

print("Person\'s name:", config_data['Person']['name'])
print("Person\'s age:", config_data['Person'].getint('age'))
print("Person\'s middle name:", config_data.get('Person', 'middle_name', fallback='I dont have a middle name'))

# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 15 16:02:30 2022

# @author: peyman
# """

# import configparser

# config = configparser.ConfigParser()

# config['Person'] = {
#     "name":"Chris",
#     "age" : "34"
#     }

# config['Run_time']={}
# config['Run_time']['start_time']='2201'
# config['Run_time']['end_time']='2023'

# with open('setting.cfg', 'w') as configfile: 
#     config.write(configfile)

"""
Config Writer

A simple script for writing key-value pairs to a configuration file.

Input Requirements:
- The input should be a dictionary containing sections as keys and dictionaries as values.
- Each inner dictionary should contain key-value pairs to be written to the configuration file.

Output Values:
- A configuration file named 'setting.cfg' containing the specified key-value pairs.

Example of Usage:

import config_writer

config_data = {
"Person": {
"name": "Chris",
"age": "34"
},
"Run_time": {
"start_time": "2201",
"end_time": "2023"
}
}

write_config(config_data)

This will be what output look like: 
    setting.cfg
    [Person]
    name = Chris
    age = 34
    
    [Run_time]
    start_time = 2201
    end_time = 2023

"""

import configparser

def write_config(config_data):
    config = configparser.ConfigParser()

    for section, data in config_data.items():
        config[section] = data

    with open('setting.cfg', 'w') as configfile: 
        config.write(configfile)




import configparser

config_data = {
"Person": {
"name": "Chris",
"age": "34"
},
"Run_time": {
"start_time": "2201",
"end_time": "2023"
}
}

write_config(config_data)


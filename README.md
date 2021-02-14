# SkyBox

SkyBox is a compact and low-cost solution to gathering local air quality data. On a local scale, air quality can greatly differ within a community, leading to negligence of areas with low air quality.

## What it does

SkyBox uses a P2.5 Dust Sensor and an Air Quality Sensor to measure, record, and transmit accurate data of the levels of particulate matter and various gasses in the immediate air to map out the air quality of local areas. This data is mapped with GPS location and used to generate an overlay on an interactive map that one can use to analyze air quality on a local scale just by checking a website.

## How it works

The SkyBox hardware is built on a custom-designed 3D-printed chassis that holds an Arduino Uno wired up to a P2.5 Dust sensor and an Air Quality sensor. The chassis was designed in Fusion 360 and can be mounted to anything from busses, to delivery vans, to drones.

The SkyBox software is a combination of Arduino and Python scripts. The Arduino code interfaces with the SkyBox to record sensor data and send it over the serial port, where it is parsed with a Python script that writes the data to a csv file and then uses the Maps API to generate the Air Quality Map. The same data is used to create the interactive public Air Quality Map as well.

## Generated Map

![Generated Map](https://github.com/shalin-jain/SkyBox-TreeHacks/blob/main/ExampleMap.jpg)

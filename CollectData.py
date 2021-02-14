import serial
import time
import Location
import csv

arduino = serial.Serial('COM5', 9600, timeout=.1)
time.sleep(1)  # give the connection a second to settle
air_quality_data = []
i = 0
while (i < 30):
    data = str(arduino.readline().decode('utf-8'))
    if data:
        data_processed = data.split(",")
        msg = 'The recorded PM2.5 Dust Concentration is '
        if data_processed[0] == '00':
            msg += "between 0 - 30 ug/m^3. There is little to no risk."
        elif data_processed[0] == '11':
            msg += "between 30 - 60 ug/m^3. Those very sensitive to dust may experience some discomfort."
        elif data_processed[0] == '22':
            msg += "between 60 - 90 ug/m^3, will be uncomfortable for those with asthma, elderly, and children."
        elif data_processed[0] == '33':
            msg += "between 90 - 120 ug/m^3. The dust is approaching dangerous levels and breathing will be uncomfortable."
        elif data_processed[0] == '44':
            msg += "between 120 - 250 ug/m^3. The air is not safe to breathe for extended periods of time."
        else:
            msg += "over 250 ug/m^3. The air is immediately hazardous to all."

        if data_processed[1] == '0':
            msg += "No significant pollutants detected."
        elif data_processed[2] == '1':
            msg += "Some pollutants detected."
        else:
            msg+= "Air is polluted."
        location_processed = Location.getLocation()
        air_quality_data.append([location_processed[0],
                             location_processed[1],
                             data_processed[0],
                             data_processed[1],
                             msg,
                             i
                             ])
        print(data_processed)
        print(location_processed)
        i += 1

with open('data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Latitude', 'Longitude', 'Dust Levels', 'Air Pollution Levels', 'Information', 'Num'])
    csvwriter.writerows(air_quality_data)


# importing required modules
import requests
import csv

# Enter api key
api_key = "AIzaSyCCm_KNFdy0nmbEwL-Q2Tbbhr5rp_OYLmI"

# url to static maps api
url = "https://maps.googleapis.com/maps/api/staticmap?"

coordinates0 = ''
coordinates1 = ''
coordinates2 = ''
coordinates3 = ''
coordinates4 = ''
coordinates5 = ''

# define coordinates from csv
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        if line['Dust Levels'] == '0':
            coordinates0 += '%7C' + line['Latitude'] + ',' + line['Longitude']
        elif line['Dust Levels'] == '1':
            coordinates1 += '%7C' + line['Latitude'] + ',' + line['Longitude']
        elif line['Dust Levels'] == '2':
            coordinates2 += '%7C' + line['Latitude'] + ',' + line['Longitude']
        elif line['Dust Levels'] == '3':
            coordinates3 += '%7C' + line['Latitude'] + ',' + line['Longitude']
        elif line['Dust Levels'] == '4':
            coordinates4 += '%7C' + line['Latitude'] + ',' + line['Longitude']
        else:
            coordinates5 += '%7C' + line['Latitude'] + ',' + line['Longitude']

# generating map image
zoom = 20
# get method of requests module, return response object
r = requests.get(url + str(zoom) + "&size=1000x1000" + "&maptype=satellite" +
                 "&markers=size:small%7Ccolor:green%7C" + coordinates0 +
                 "&markers=size:small%7Ccolor:yellow%7C" + coordinates1 +
                 "&markers=size:small%7Ccolor:0xf3c667%7C" + coordinates2 +
                 "&markers=size:small%7Ccolor:0xf89f65%7C" + coordinates3 +
                 "&markers=size:small%7Ccolor:0xfb8177%7C" + coordinates4 +
                 "&markers=size:small%7Ccolor:0xff4f69%7C" + coordinates5 +
                 "&key=" + api_key)

# wb mode is stand for write binary mode
f = open('dustMap.jpg ', 'wb')

# r.content gives image
f.write(r.content)

# save and close the file
f.close()

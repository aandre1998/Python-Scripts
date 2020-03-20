### Initialize data set path, specify which columns contain latitude and longitude,
### whether your data set has headers
### (NOTE: counting columns starts at 0)

DATA = 'data.csv'
LAT_COLUMN = 5 # Latitude column number
LONG_COLUMN = 6 # Longitude column number
HEADERS = True # Does your data have headers?

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Zip Code Finder")

latlongs = []

f = open(DATA, 'r')

### Remove all data except for latitude and longitude
for line in f:
    cells = line.split(",")
    latlongs.append((cells[LAT_COLUMN], cells[LONG_COLUMN]))

f.close()

zips = []

if HEADERS:
    del latlongs[0]

### Send each lat/long to google API, get full address, parse each address for zip code
for point in latlongs:
    address = str(geolocator.reverse(point[0] + " " + point[1], timeout=1000))
    print(address)
    cells = address.split(",")
    zips.append(cells[-2])

f = open('zipcodes.csv','w+',encoding='utf-8')

### Write to zipcodes.csv, creating a single column of all zip codes
for i in zips:
    f.write(i + "\n")
    print(i)

f.close()

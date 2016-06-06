import gmplot
import csv

lats = []
lons = []

with open("./assault_locations.csv", 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row[6]
        lat, lon = gmplot.GoogleMapPlotter.geocode(row[6] + " , Charlottesville, Virginia")
        lats.append(lat)
        lons.append(lon)

gmap = gmplot.GoogleMapPlotter.from_geocode("Charlottesville, Virginia")
gmap.scatter(lats,lons, 'k', marker=True)

#gmap.heatmap(lats,lons)

print lats, lons

gmap.draw("markers.html")
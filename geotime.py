import shapefile

f = shapefile.Reader('shapefiles/intersections.shp')
data = f.shapeRecords()
print(data[0].shape.__geo_interface__)
print(data[0].__geo_interface__)
print(data.__geo_interface__)

f = shapefile.Reader('shapefiles/blockgroups.shp')
data = f.shapeRecords()
print(data[0].shape.__geo_interface__)
print(data[0].__geo_interface__)
print(data.__geo_interface__)

f = shapefile.Reader('shapefiles/points.shp')
data = f.shapeRecords()
print(data[0].shape.__geo_interface__)
print(data[0].__geo_interface__)
print(data.__geo_interface__)
# iface lets us interact with QGIS objects
#.activeLayer() accesses the currently selected layer
layer = iface.activeLayer()
# dir() method tells us what tools we can call on a given object
dir(layer)
# we can use a for loop to iterate over all the features in a layer
for f in layer.getFeatures():
  print(f)
  
# Adding world map
v_layer = iface.addVectorLayer("/Applications/QGIS3.10.app/Contents/Resources/resources/data/world_map.gpkg", 'countries', 'ogr')

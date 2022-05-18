### Goal of this script is to show how to import data using Python

import os 
from qgis.core import (
    QgsVectorLayer
)
from osgeo import ogr
    
#Add countries shapefile

path_to_blayer = "/Applications/QGIS-LTR.app/Contents/Resources/resources/data/world_map.gpkg"
gpkg_layers = [l.GetName() for l in ogr.Open(path_to_blayer)]
print(gpkg_layers)

def add_gpkg_layer(gpkg, layer):
    layers = [l.GetName() for l in ogr.Open(gpkg)]
    if layer in layers:
        iface.addVectorLayer(gpkg + "|layername=" + layer, layer, 'ogr')
    else: 
        print('Error: there is no layer named "{}" in {}!'.format(layer, gpkg))
def add_layers_from_gpkg(gpkg, layers):
    for layer in layers:
        add_gpkg_layer(gpkg, layer)

add_layers_from_gpkg(path_to_blayer, ['countries', 'states_provinces'])

#Add census shapefiles

path_to_clayer = "/Users/nickbarber/OneDrive - University Of Cambridge/PhD Research/Talks/GIS for Geoscientists/qgis/GIS_Base_Layers/ecu_popcensus.shp"

vlayer = QgsVectorLayer(path_to_clayer, "Census layer", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    QgsProject.instance().addMapLayer(vlayer)
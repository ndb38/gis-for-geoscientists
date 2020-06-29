import qgis.analysis
import qgis.core
import numpy as np
    
for i in np.arange(4, 18):
    
    layer = qgis.utils.iface.activeLayer() 
    layer_data = qgis.analysis.QgsInterpolator.LayerData()

    layer_data.vectorLayer = layer
    layer_data.zCoordInterpolation=False
    layer_data.interpolationAttribute = i
    layer_data.mInputType = 1

    idw_interpolator = qgis.analysis.QgsIDWInterpolator([layer_data])

    export_path = "/Users/nickbarber/OneDrive - University Of Cambridge/PhD Research/Talks/McGill Workshop and Talk 2020/qgis/Fluid Chem/script/"

    rect = layer.extent()
    res = 100
    ncol = int( ( rect.xMaximum() - rect.xMinimum() ) / res )
    nrows = int( (rect.yMaximum() - rect.yMinimum() ) / res)
    
    output = qgis.analysis.QgsGridFileWriter(interpolator = idw_interpolator, outputPath = export_path, extent = rect, nCols = ncol, nRows = nrows)
    output.writeFile()
    
    #qgis.utils.iface.addRasterLayer(export_path, "interpolation_output_{}".format(i)) 
import rasterio
import matplotlib.pyplot as plt
import numpy as np

heatmap_raster_path = "C:\\Users\\echoe\\OneDrive\\Desktop\\Geospatial Tech 25-26\\heat_map-main\\heat_map-main\\data\\output\\f_deviation_smooth.tif"
with rasterio.open(heatmap_raster_path) as src:
    heat_map = src.read(1)
    
    if src.nodata is not None:
        heat_map = np.ma.masked_equal(heat_map, src.nodata)
    else:
        heat_map = np.ma.masked_less(heat_map, -100)

    plt.figure(figsize=(9, 8))
    

    plt.imshow(heat_map, cmap='turbo')
    
    plt.title("NYC Urban Heat Map (Mean Surface Temperature 2020–2022)")
    
    plt.colorbar(label="Deviation from the Mean")
    plt.tight_layout()
    plt.grid()
    plt.show()
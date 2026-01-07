import rasterio

tiff_path = "C:\\Users\\echoe\\OneDrive\\Desktop\\Geospatial Tech 25-26\\heat_map-main\\heat_map-main\\data\\input\\surfacetemperature_median_2020_2022.tif"
with rasterio.open(tiff_path) as src:
    raster_array = src.read(1)       
    profile = src.profile     

print(raster_array.shape)
print(raster_array[0, 0])
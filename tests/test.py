import rasterio

with rasterio.open("surface_temp_mean.tif") as src:
    data = src.read(1)   # first band = temperature values

print(data)

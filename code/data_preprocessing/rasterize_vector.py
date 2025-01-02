import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask
import numpy as np

# Load vector data (shapefile)
vector_file = 'data/vector_data.shp'
gdf = gpd.read_file(vector_file)

# Define raster specifications (same as input raster)
raster_file = 'data/raw_raster.tif'
with rasterio.open(raster_file) as src:
    out_shape = (src.height, src.width)
    transform = src.transform
    crs = src.crs
    dtype = np.uint8

# Rasterize the vector data
mask = geometry_mask(gdf.geometry, transform=transform, invert=True, out_shape=out_shape)

# Create and save the rasterized output
output_raster = 'data/processed/rasterized_output.tif'
with rasterio.open(output_raster, 'w', driver='GTiff', count=1, dtype=dtype, crs=crs, transform=transform, width=out_shape[1], height=out_shape[0]) as dest:
    dest.write(mask.astype(dtype), 1)

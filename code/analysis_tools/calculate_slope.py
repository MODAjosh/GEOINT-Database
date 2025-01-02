import rasterio
import numpy as np
from rasterio.enums import Resampling
from rasterio import Affine

# Load the DEM raster file
src_file = 'processed_data/dem.tif'

with rasterio.open(src_file) as src:
    # Read the DEM data
    dem_data = src.read(1)

    # Calculate the slope
    x_res, y_res = src.res
    x_slope = np.gradient(dem_data, axis=1) / x_res
    y_slope = np.gradient(dem_data, axis=0) / y_res
    slope = np.sqrt(x_slope**2 + y_slope**2)

    # Write the slope result to a new raster file
    slope_file = 'processed_data/slope.tif'
    with rasterio.open(slope_file, 'w', driver='GTiff', count=1, dtype=slope.dtype,
                       crs=src.crs, transform=src.transform) as dst:
        dst.write(slope, 1)

print("Slope calculation complete and saved.")

import rasterio
import numpy as np

# Open raster data
raster_file = 'data/raw_raster.tif'
with rasterio.open(raster_file) as src:
    data = src.read(1)

    # Normalize raster values to the range [0, 1]
    min_value = np.min(data)
    max_value = np.max(data)
    normalized_data = (data - min_value) / (max_value - min_value)

    # Save the normalized raster
    normalized_raster = 'data/processed/normalized_raster.tif'
    with rasterio.open(normalized_raster, 'w', driver='GTiff', count=1, dtype=str(data.dtype), crs=src.crs, transform=src.transform, width=src.width, height=src.height) as dest:
        dest.write(normalized_data, 1)

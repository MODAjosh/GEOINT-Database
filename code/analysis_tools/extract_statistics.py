import rasterio
import numpy as np

# Load raster data
raster_file = 'processed_data/dem.tif'

with rasterio.open(raster_file) as src:
    # Read the raster data
    data = src.read(1)

    # Calculate statistics
    mean_value = np.mean(data)
    median_value = np.median(data)
    max_value = np.max(data)
    min_value = np.min(data)

    # Print the statistics
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")

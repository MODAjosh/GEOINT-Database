import rasterio
import numpy as np

# Load the red and NIR bands from a multi-band raster (e.g., Landsat)
red_band = 'raw_data/landsat_red.tif'
nir_band = 'raw_data/landsat_nir.tif'

with rasterio.open(red_band) as red_src, rasterio.open(nir_band) as nir_src:
    # Read the bands
    red = red_src.read(1)
    nir = nir_src.read(1)

    # Calculate NDVI
    ndvi = (nir - red) / (nir + red)

    # Save the NDVI result to a new file
    ndvi_file = 'processed_data/ndvi.tif'
    with rasterio.open(ndvi_file, 'w', driver='GTiff', count=1, dtype=ndvi.dtype,
                       crs=red_src.crs, transform=red_src.transform) as dst:
        dst.write(ndvi, 1)

print("NDVI calculation complete and saved.")

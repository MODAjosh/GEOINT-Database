import rasterio

# Input raster data (can be any format)
input_raster = 'data/raw_raster.xyz'

# Open the input raster file
with rasterio.open(input_raster) as src:
    # Create an output GeoTIFF file
    output_raster = 'data/processed/output_raster.tif'
    with rasterio.open(output_raster, 'w', driver='GTiff', count=src.count, dtype=src.dtypes[0], crs=src.crs, transform=src.transform, width=src.width, height=src.height) as dest:
        dest.write(src.read())

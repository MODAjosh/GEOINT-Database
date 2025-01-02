import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling

# Input raster file
src_file = 'raw_data/landsat_2020.tif'
dst_file = 'processed_data/landsat_2020_reprojected.tif'

# Open the source raster
with rasterio.open(src_file) as src:
    # Define the target CRS (EPSG:4326)
    transform, width, height = calculate_default_transform(
        src.crs, 'EPSG:4326', src.width, src.height, *src.bounds)
    
    # Create the destination file with the new CRS
    with rasterio.open(dst_file, 'w', driver='GTiff', count=src.count,
                       dtype=src.dtypes[0], crs='EPSG:4326', transform=transform,
                       width=width, height=height) as dst:
        for i in range(1, src.count + 1):
            reproject(
                source=rasterio.band(src, i),
                destination=rasterio.band(dst, i),
                src_transform=src.transform,
                src_crs=src.crs,
                dst_transform=transform,
                dst_crs='EPSG:4326',
                resampling=Resampling.nearest)

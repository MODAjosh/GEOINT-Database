# Data Preprocessing Scripts

This directory contains scripts used for transforming raw geospatial data into a format that can be analyzed. Data preprocessing is an essential step before performing any geospatial analysis, as it ensures the data is clean and ready for insights. 

Proper data preprocessing enables better accuracy and efficiency during geospatial analysis and decision-making processes.

## Common Data Processing Tasks

Here are some of the common data preprocessing tasks included in this directory:

- **Shapefile to GeoJSON Conversion**: Converts shapefiles to GeoJSON for easier manipulation in web maps.
- **Raster Reprojection**: Reprojects raster datasets to a common coordinate reference system (CRS), ensuring consistency when integrating multiple data sources.
- **Outlier Removal**: Identifies and removes outliers from GPS or sensor data that could negatively affect analysis accuracy.
- **Data Merging**: Merges datasets from different sources, formats, or coordinate systems into a single, cohesive dataset.
- **Data Cleaning**: Cleans up invalid geometries, handles missing data, and prepares datasets for further analysis.

## Example Script: `reproject_raster.py`

This script demonstrates how to reproject a raster file from one CRS to another. Reprojecting ensures that all datasets are in a consistent CRS, which is essential for accurate analysis and map creation.

### Script Explanation:

```python
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

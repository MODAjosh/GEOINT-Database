# Data Preprocessing Scripts

This directory contains scripts used for cleaning, transforming, and preparing raw geospatial data for analysis. These scripts perform tasks such as reformatting, spatial indexing, and reprojecting geospatial data.

## Common Data Processing Tasks:
- **Shapefile to GeoJSON Conversion**: Convert shapefiles to GeoJSON for easier manipulation.
- **Raster Reprojection**: Reproject raster datasets to a common coordinate reference system.
- **Outlier Removal**: Identify and remove outliers from GPS or sensor data.

### Example Processing Script
```python
import geopandas as gpd

# Read shapefile
shapefile = gpd.read_file('raw_data/urban_area.shp')

# Reproject to EPSG:4326
shapefile = shapefile.to_crs(epsg=4326)

# Save as GeoJSON
shapefile.to_file('processed_data/urban_area.geojson', driver='GeoJSON')

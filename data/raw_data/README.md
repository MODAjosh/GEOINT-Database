# Raw Geospatial Data

This directory contains the raw geospatial data used for analysis in this repository. All datasets are stored in their original format as received, before any preprocessing or transformations. Raw data can be complex, but it forms the foundation of any geospatial analysis.

## Datasets Included:
- **Satellite Imagery**: GeoTIFF files from satellite missions like Landsat, Sentinel, etc.
- **Drone Survey Data**: GPS data, LiDAR data, and camera sensor data collected using drones.
- **Shapefiles**: Geospatial vector data (points, lines, and polygons) for various locations.

### Example Data Files:
- `landsat_2020.tif` - GeoTIFF of satellite imagery for urban area analysis.
- `drone_gps_data.csv` - CSV file containing GPS coordinates from a drone survey.

### Important Notes:
- Raw data can contain noise, missing values, or errors. Be sure to clean and preprocess this data before using it for analysis.
- Always refer to the metadata files (in `metadata/`) for information on the data’s source, collection methods, and limitations.

## Adding New Data
1. Upload new raw geospatial datasets into this directory.
2. Ensure that the metadata for the new datasets is created and saved in the `metadata/` folder.
3. Follow naming conventions for consistency and ease of use.

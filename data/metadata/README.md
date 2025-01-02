# Geospatial Data Metadata

This directory contains metadata files for each dataset stored in the `raw_data/` and `processed_data/` directories. Metadata provides essential information about the source, collection, transformation, and usage of each dataset.

## Metadata Fields
- **Source**: The origin of the data (e.g., satellite, drone, field surveys).
- **Collection Date**: The date when the data was collected.
- **Data Type**: The type of data (e.g., raster, vector, GPS coordinates).
- **Description**: A brief description of the dataset.
- **Data Processing**: Steps taken to clean, transform, or project the data.
  
### Example Metadata File:
```json
{
  "source": "Landsat 8",
  "collection_date": "2022-05-01",
  "data_type": "Raster",
  "description": "Satellite imagery of urban areas in the region.",
  "data_processing": "Reprojected from WGS84 to NAD83, clipped to study area."
}

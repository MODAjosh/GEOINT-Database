# Processed Geospatial Data

This directory contains pre-processed and cleaned geospatial data that is ready for analysis. Preprocessing steps may include data cleaning, transformation, reformatting, and projection.

## Datasets Included:
- **Urban Heat Island Analysis**: Processed temperature data and associated geospatial features.
- **Topographic Maps**: Processed topographic map data aligned with other geospatial layers.

### Example Data Files:
- `urban_heat_islands_2021.geojson` - A GeoJSON file containing the results of an urban heat island study, processed from raw satellite thermal imagery.
- `topographic_map_2020.shp` - Shapefile of topographic features like rivers, roads, and elevation contours.

### Important Notes:
- Processed data is easier to use for analysis but may have some simplifications or assumptions made during the processing.
- Ensure the projection and coordinate reference system (CRS) is consistent across datasets.

## Adding New Processed Data
1. After processing raw data, upload the cleaned datasets to this directory.
2. Add relevant metadata about the transformation steps in the `metadata/` folder.
3. Document any assumptions or simplifications made during preprocessing.

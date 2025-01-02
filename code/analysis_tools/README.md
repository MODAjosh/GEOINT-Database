# Geospatial Analysis Tools

This directory contains scripts for performing spatial analysis on the geospatial datasets. Analysis tasks can include buffer creation, distance calculations, area analysis, and more.

## Common Analysis Tasks:
- **Buffer Zone Creation**: Generate buffer zones around specified features.
- **Distance Calculations**: Calculate distances between points, lines, or polygons.
- **Overlay Analysis**: Analyze overlapping geospatial layers (e.g., land use and urban heat islands).

### Example Analysis Script
```python
import geopandas as gpd

# Load data
urban_area = gpd.read_file('processed_data/urban_area.geojson')

# Create a 500-meter buffer
urban_buffer = urban_area.buffer(500)

# Save the result
urban_buffer.to_file('results/urban_buffer.geojson', driver='GeoJSON')

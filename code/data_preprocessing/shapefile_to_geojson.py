import geopandas as gpd

# Input shapefile
shapefile = 'shapefiles/your_shapefile.shp'
output_geojson = 'processed_data/your_data.geojson'

# Load the shapefile using GeoPandas
gdf = gpd.read_file(shapefile)

# Convert to GeoJSON and save
gdf.to_file(output_geojson, driver='GeoJSON')

print(f"Shapefile {shapefile} has been converted to GeoJSON and saved to {output_geojson}.")


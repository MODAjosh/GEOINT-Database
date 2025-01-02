import geopandas as gpd

# Load data
gdf = gpd.read_file('processed_data/merged_shapefile.shp')

# Calculate buffer zones (e.g., 100 meters around each feature)
gdf['buffer'] = gdf.geometry.buffer(100)  # Adjust the distance as needed

# Save the buffer zones as a new shapefile
gdf[['buffer']].to_file('processed_data/buffer_zones.shp')

print("Buffer zones have been calculated and saved.")

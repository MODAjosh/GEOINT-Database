import geopandas as gpd

# Load geospatial data (e.g., polygons)
gdf = gpd.read_file('processed_data/merged_shapefile.shp')

# Calculate the centroids of the polygons
gdf['centroid'] = gdf.geometry.centroid

# Save the centroids as a new shapefile
gdf[['centroid']].to_file('processed_data/centroids.shp')

print("Centroids have been calculated and saved.")

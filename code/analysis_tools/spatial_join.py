import geopandas as gpd

# Load two geospatial datasets
gdf_points = gpd.read_file('processed_data/points.shp')
gdf_polygons = gpd.read_file('processed_data/polygons.shp')

# Perform spatial join (find points within polygons)
joined_gdf = gpd.sjoin(gdf_points, gdf_polygons, how='inner', op='within')

# Save the results
joined_gdf.to_file('processed_data/spatial_joined_results.shp')

print("Spatial join completed and results saved.")

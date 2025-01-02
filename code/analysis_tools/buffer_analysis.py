import geopandas as gpd

# Load geospatial data (shapefile)
gdf = gpd.read_file('data/shapefiles/my_shapefile.shp')

# Create a 100-meter buffer around each feature
gdf['buffer'] = gdf.geometry.buffer(100)

# Save the resulting buffered geometries
gdf.to_file('results/buffered_geometries.shp')

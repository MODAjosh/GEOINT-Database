import geopandas as gpd

# Load vector data (e.g., shapefile)
vector_file = 'data/vector_data.shp'
gdf = gpd.read_file(vector_file)

# Create a buffer around each geometry (e.g., 500 meters)
buffered_gdf = gdf.buffer(500)

# Save the buffered geometries to a new shapefile
buffered_gdf.to_file('data/processed/buffered_vector_data.shp')

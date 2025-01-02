import geopandas as gpd

# Load geospatial data
gdf = gpd.read_file('data/shapefiles/my_shapefile.shp')

# Reproject to a new CRS (e.g., EPSG:4326)
gdf = gdf.to_crs(epsg=4326)

# Save the reprojected data
gdf.to_file('results/reprojected_shapefile.shp')

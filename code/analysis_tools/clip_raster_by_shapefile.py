import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Load shapefile (polygon for clipping)
shapefile = 'processed_data/clip_polygon.shp'
gdf = gpd.read_file(shapefile)

# Load raster data (e.g., DEM)
raster_file = 'processed_data/dem.tif'
with rasterio.open(raster_file) as src:
    # Mask the raster with the shapefile geometry
    geometry = [gdf.geometry.unary_union]  # Convert to a single geometry
    out_image, out_transform = mask(src, geometry, crop=True)
    
    # Save the clipped raster
    clipped_raster_file = 'processed_data/clipped_dem.tif'
    with rasterio.open(clipped_raster_file, 'w', driver='GTiff', count=1,
                       dtype=out_image.dtype, crs=src.crs, transform=out_transform) as dst:
        dst.write(out_image, 1)

print("Raster clipped by shapefile and saved.")

# Geospatial Analysis Tools

This directory contains a collection of Python scripts designed to perform spatial analysis on geospatial datasets. The tools cover a wide range of analysis tasks such as buffer creation, distance calculations, area analysis, raster processing, and more. These tools are essential for professionals in Geospatial Intelligence (GEOINT), helping them derive insights and make informed decisions.

## Common Analysis Tasks and Use Cases

### **Buffer Zone Creation**
- **Use Case:** In urban planning, you may need to create buffer zones around critical infrastructure, such as power plants, to determine the area within a certain distance that could be affected by an incident (e.g., hazardous material spills or radiation leakage). Buffer zones can also be used in environmental monitoring to protect endangered species by marking zones around critical habitats.

### **Distance Calculations**
- **Use Case:** Distance calculations are crucial in logistics and transportation planning. For instance, in supply chain management, determining the distance between distribution centers and retail locations can optimize delivery routes. Similarly, this tool can be used in disaster response to calculate distances between rescue teams and affected areas.

### **Overlay Analysis**
- **Use Case:** Overlay analysis is widely used in land-use planning and environmental management. For example, in determining the risk of urban heat islands, this tool can overlay land use data with temperature data to identify urban areas that experience higher heat due to the concentration of buildings and reduced green spaces. It can also be used for conservation, where it overlays protected areas with deforestation data to identify potential threats to biodiversity.

### **Slope Calculation**
- **Use Case:** In agriculture, slope calculation is used to identify the suitability of land for farming or planting. For instance, certain crops may require specific slopes for efficient water drainage. Similarly, in civil engineering, slope calculations can help determine the stability of terrain for construction projects, such as roads or buildings.

### **Normalized Difference Vegetation Index (NDVI)**
- **Use Case:** NDVI is commonly used in agriculture and forestry to monitor vegetation health. Farmers use NDVI to track crop health throughout the growing season, adjusting irrigation and fertilization practices accordingly. Additionally, NDVI is crucial in disaster management, where it helps assess the impact of natural disasters like wildfires or floods on vegetation.

### **Raster Clipping**
- **Use Case:** Raster clipping is used to focus analysis on a specific region of interest, such as a city or protected area, from a larger dataset. For example, in urban planning, a raster dataset showing land elevation might be clipped to the city boundary to analyze the terrain within the urban area. Similarly, in environmental monitoring, raster data showing forest cover can be clipped to study a particular national park or wildlife reserve.

### **Outlier Removal**
- **Use Case:** Outlier removal is used to clean sensor data or GPS data in situations where inaccurate readings could distort analysis. For example, in drone-based surveying, outlier removal can help clean data collected from GPS sensors or cameras to ensure accurate mapping and 3D modeling of the surveyed area.

### **Geospatial Statistics Extraction**
- **Use Case:** In urban studies, extracting statistical data (e.g., average temperature, land cover percentage) from a raster dataset can provide insights into the state of urban development and environmental conditions. For instance, a city planner may analyze satellite imagery to extract statistics on land cover types, such as the percentage of urbanized areas, green spaces, and water bodies.

## How to Use These Tools

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/GEOINT-Database.git
cd GEOINT-Database
```

2. **Install necessary dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run an analysis tool:**
   - Navigate to the `code/analysis_tools/` folder.
   - Choose a script that corresponds to your analysis needs (e.g., `calculate_slope.py`).
   - Modify the script with the appropriate file paths to your geospatial data.
   - Run the script to perform the analysis.

4. **View results:**
   - The output of most tools will be saved in the `results/` folder or as new files in the `processed_data/` folder.

## Dependencies

The following Python libraries are required for running these tools:

- `geopandas`
- `rasterio`
- `numpy`
- `matplotlib`
- `shapely`

You can install them using:

```bash
pip install -r requirements.txt
```

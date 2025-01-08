# Geospatial Analysis Tools and Preprocessing Scripts

This repository contains a comprehensive collection of Python tools for geospatial data analysis and preprocessing. These tools are designed for professionals in Geospatial Intelligence (GEOINT) and related fields, enabling efficient handling of geospatial datasets for analysis, decision-making, and insights.

---

## Features

### Geospatial Analysis Tools
These tools perform advanced geospatial analyses, including:
- **Buffer Zone Creation**: Identify areas affected by incidents or zones requiring protection.
- **Distance Calculations**: Determine distances between features for logistics, disaster response, or planning.
- **Overlay Analysis**: Combine datasets to identify risks, patterns, or opportunities (e.g., heat islands, biodiversity threats).
- **Slope Calculation**: Assess terrain stability for agriculture, construction, or disaster management.
- **NDVI (Normalized Difference Vegetation Index)**: Monitor vegetation health for agriculture or forestry applications.
- **Raster Clipping**: Focus analysis on specific regions of interest (e.g., cities, parks).
- **Geospatial Statistics Extraction**: Derive insights from raster datasets, such as average land cover or temperature.

### Data Preprocessing Scripts
Preprocessing ensures raw geospatial data is clean and ready for analysis. Tasks include:
- **Shapefile to GeoJSON Conversion**: Prepare data for web maps and modern tools.
- **Raster Reprojection**: Align data from different sources into a common CRS.
- **Outlier Removal**: Clean noisy GPS or sensor data for accurate analysis.
- **Data Merging**: Combine datasets into a single, cohesive format.
- **Data Cleaning**: Fix invalid geometries and handle missing data.
- **Rasterization of Vector Data**: Convert vector datasets into raster format for grid-based spatial analysis.

---

## Common Use Cases

### Analysis Tools
1. **Urban Planning**: Create buffer zones around critical infrastructure to assess impact zones.
2. **Agriculture**: Monitor crop health using NDVI or calculate slopes for water drainage.
3. **Disaster Management**: Analyze distances between affected areas and rescue teams or assess vegetation loss after wildfires.
4. **Environmental Monitoring**: Overlay protected areas with deforestation data to identify conservation priorities.

### Preprocessing Scripts
1. **Web Mapping**: Convert shapefiles to GeoJSON for use in applications like Leaflet or Mapbox.
2. **Dataset Integration**: Reproject raster data to ensure consistency across multiple datasets.
3. **Sensor Data Cleaning**: Remove GPS or sensor noise for drone-based mapping and analysis.
4. **Raster Analysis**: Rasterize vector data for use in classification or proximity calculations.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/GEOINT-Database.git
   cd GEOINT-Database
   ```

2. **Install Dependencies**:
   Use the included `requirements.txt` file to install all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

### Running Analysis Tools
1. Navigate to the `code/analysis_tools` folder.
2. Choose a script that corresponds to your analysis needs (e.g., `buffer_creation.py`).
3. Modify the script to point to your data files.
4. Run the script to generate results.

### Running Preprocessing Scripts
1. Navigate to the `code/preprocessing` folder.
2. Choose the appropriate preprocessing script (e.g., `convert_shapefile_to_geojson.py`).
3. Adjust input and output file paths as needed.
4. Execute the script to preprocess your data.

---

## Output Files

Results from the tools and scripts are saved in the following locations:
- **Processed Data**: Cleaned and processed datasets are stored in the `processed_data/` folder.
- **Results**: Outputs from analysis tools (e.g., maps, GeoTIFFs) are saved in the `results/` folder.

---

## Dependencies

This repository requires the following Python libraries:
- **Geospatial Libraries**:
  - `geopandas`
  - `rasterio`
  - `shapely`
  - `pyproj`
- **Data Analysis and Visualization**:
  - `pandas`
  - `numpy`
  - `matplotlib`

Install them using:
```bash
pip install -r requirements.txt
```

---

## File Organization

```
.
├── raw_data/               # Unprocessed datasets
├── processed_data/         # Preprocessed datasets
├── results/                # Output files from analysis tools
├── code/                   # Scripts for analysis and preprocessing
│   ├── analysis_tools/     # Analysis scripts (e.g., NDVI, slope calculation)
│   ├── preprocessing/      # Preprocessing scripts (e.g., reprojection, rasterization)
├── requirements.txt        # Python library requirements
└── README.md               # Documentation
```

---

## License

This repository is licensed under the MIT License. Please provide credit to **Joshua Stinson** when using or redistributing the tools or code in this repository.

---

Let me know if you'd like further adjustments!

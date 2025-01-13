## Geospatial Analysis Tools and Preprocessing Scripts

This repository contains a collection of Python tools and scripts for geospatial data analysis and preprocessing. It is designed to assist in the manipulation, analysis, and visualization of geospatial data, with a focus on raster and vector data processing, geospatial analysis, and data preprocessing. The tools are tailored for professionals in Geospatial Intelligence (GEOINT) and related fields, enabling efficient management of geospatial datasets for decision-making and insights.

### Features

#### Geospatial Analysis Tools

These advanced tools are designed for a range of geospatial analyses, including:

- **Buffer Zone Creation**: Define zones impacted by incidents or areas requiring protection.
- **Distance Calculations**: Calculate distances between features for logistics, disaster response, or planning purposes.
- **Overlay Analysis**: Merge datasets to identify patterns, risks, or opportunities (e.g., heat islands, biodiversity threats).
- **Slope Calculation**: Evaluate terrain stability for agriculture, construction, or disaster management.
- **NDVI (Normalized Difference Vegetation Index)**: Monitor vegetation health for agriculture or forestry.
- **Raster Clipping**: Focus your analysis on specific regions of interest (e.g., cities, parks).
- **Geospatial Statistics Extraction**: Extract key insights from raster datasets, such as average land cover or temperature.

#### Data Preprocessing Scripts

Preprocessing scripts ensure raw geospatial data is properly cleaned and prepared for analysis, including:

- **Shapefile to GeoJSON Conversion**: Prepare data for web mapping and modern tools.
- **Raster Reprojection**: Standardize coordinate reference systems across different data sources.
- **Outlier Removal**: Clean noisy GPS or sensor data for more accurate analysis.
- **Data Merging**: Integrate multiple datasets into a single cohesive format.
- **Data Cleaning**: Resolve invalid geometries and handle missing data.
- **Rasterization of Vector Data**: Convert vector data into raster format for grid-based spatial analysis.

### Common Use Cases

#### Analysis Tools
- **Urban Planning**: Create buffer zones around critical infrastructure to evaluate impact zones.
- **Agriculture**: Track crop health with NDVI or assess slopes for optimal water drainage.
- **Disaster Management**: Calculate distances between affected regions and rescue teams or evaluate vegetation loss post-wildfire.
- **Environmental Monitoring**: Overlay deforestation data with protected areas to prioritize conservation efforts.

#### Preprocessing Scripts
- **Web Mapping**: Convert shapefiles to GeoJSON for integration with tools like Leaflet or Mapbox.
- **Dataset Integration**: Reproject raster data to ensure consistency across multiple datasets.
- **Sensor Data Cleaning**: Remove noise from GPS or sensor data for more accurate drone-based mapping.
- **Raster Analysis**: Rasterize vector datasets for classification or proximity analysis.

### Directory Structure

The project is organized into the following main directories:

```plaintext
.
├── raw_data/               # Unprocessed datasets
├── processed_data/         # Preprocessed datasets
├── results/                # Output files from analysis tools
├── code/                   # Scripts for analysis, preprocessing, UI, and documentation
│   ├── analysis_tools/     # Analysis scripts (e.g., NDVI, slope calculation)
│   ├── preprocessing/      # Preprocessing scripts (e.g., reprojection, rasterization)
│   ├── ui/                 # UI application for running scripts
│   │   └── ui_launcher.py  # Main script to launch the UI
│   ├── requirements.txt    # Python library requirements
│   └── README.md           # Documentation for repository
```

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/GEOINT-Database.git
   cd GEOINT-Database
   ```

2. **Install Dependencies:**
   Use the provided `requirements.txt` file to install all necessary libraries:

   ```bash
   pip install -r code/requirements.txt
   ```

### How to Use

#### Running Analysis Tools

1. Navigate to the `code/analysis_tools` folder.
2. Select a script corresponding to your analysis needs (e.g., `buffer_analysis.py`).
3. Modify the script to reference your data files.
4. Run the script to generate results.

#### Running Preprocessing Scripts

1. Navigate to the `code/preprocessing` folder.
2. Choose the appropriate preprocessing script (e.g., `convert_shapefile_to_geojson.py`).
3. Adjust input and output file paths as needed.
4. Execute the script to preprocess your data.

#### Accessing Scripts Through the User Interface (UI)

To provide a more user-friendly experience, you can access and run the scripts via a simple graphical user interface (GUI). The UI allows you to select input files, configure script parameters, and visualize results without manually editing scripts.

1. **Start the UI Application:**
   Launch the UI by running the following command:

   ```bash
   python code/ui/ui_launcher.py
   ```

2. **Using the UI:**
   - Upon launching, the UI will display a list of available analysis and preprocessing scripts.
   - Choose the script you want to run (e.g., Buffer Zone Creation, Shapefile to GeoJSON Conversion).
   - Input file options: Select input files (e.g., shapefiles or raster data) via the file picker dialog.
   - Configure parameters: Adjust any necessary parameters (e.g., buffer zone radius, target coordinate reference system) using input fields or dropdowns.
   - Run the script: Press the "Run" button to execute the script. Results will be displayed in the UI and saved in the `results/` folder.

3. **Viewing Results:**
   Once a script has completed, you can view the results directly in the UI. Depending on the script, outputs may include maps, charts, or data tables.

### Output Files

Results are saved in the following directories:

- **Processed Data**: Cleaned and processed datasets are stored in the `processed_data/` folder.
- **Results**: Outputs from analysis tools (e.g., maps, GeoTIFFs) are saved in the `results/` folder.

### Troubleshooting

1. **ModuleNotFoundError**
   - Ensure all dependencies are installed by running:

   ```bash
   pip install -r code/requirements.txt
   ```

2. **Permission Denied Error**
   - Ensure you have the appropriate permissions for the files and directories involved.

3. **Invalid File Format**
   - Verify the format of the input files and ensure they match the expected formats.

4. **Script Execution Error**
   - Check the error message for details and review file paths and dependencies.

5. **UI Program Not Launching**
   - Ensure the necessary GUI libraries (e.g., Tkinter, PyQt) are installed:

   ```bash
   pip install tk
   ```

### License

This repository is licensed under the MIT License. Please credit Joshua Stinson when using or redistributing any tools or code from this repository.

---

This version now reflects the correct directory structure, where the UI, requirements, and README files are all located under the `code` directory. Let me know if further adjustments are needed!

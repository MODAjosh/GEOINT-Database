# GEOINT-Code-Repository

This repository contains a collection of tools and scripts for geospatial data analysis and preprocessing. It is designed to assist in the manipulation, analysis, and visualization of geospatial data, with a focus on raster and vector data processing, geospatial analysis, and data preprocessing using Python.

## Directory Structure

The project is organized into the following main directories:

- **UI_Program/**: Contains the user interface program for running and interacting with the geospatial scripts.
    - `script_runner_UI.Vr.003.py`: Main script for running the UI program.

- **analysis_tools/**: Contains various Python scripts for performing geospatial analysis.
    - `buffer_analysis.py`: Script for performing buffer analysis on spatial data.
    - `calculate_buffer_zone.py`: Computes buffer zones for given geometries.
    - `calculate_centroid.py`: Calculates the centroid of a given spatial feature.
    - `calculate_distance.py`: Calculates the distance between spatial features.
    - `calculate_slope.py`: Computes the slope of a raster dataset.
    - `clip_raster_by_shapefile.py`: Clips a raster dataset using a shapefile.
    - `extract_statistics.py`: Extracts statistics from geospatial data.
    - `ndvi_calculation.py`: Calculates NDVI (Normalized Difference Vegetation Index) from remote sensing data.
    - `perform_geospatial_analysis.py`: Main script to perform various geospatial analysis tasks.
    - `requirements.txt`: Lists the required Python packages for the analysis tools.
    - `spatial_join.py`: Performs spatial join operations on spatial datasets.
    - `Geodesic_Distance_Calculation_and_Visualisation.md`: Documentation for geodesic distance calculations and visualization.

- **data_preprocessing/**: Contains scripts for preprocessing geospatial data.
    - `buffer_vector_data.py`: Preprocesses vector data to create buffers.
    - `clip_raster_by_polygon.py`: Clips raster data by a polygon shapefile.
    - `clip_shapefile_by_polygon.py`: Clips shapefile data by a polygon.
    - `merge_data.py`: Merges multiple datasets.
    - `normalize_raster.py`: Normalizes raster data.
    - `rasterize_vector.py`: Converts vector data to raster format.
    - `reformat_to_geotiff.py`: Converts geospatial data to GeoTIFF format.
    - `remove_outliers.py`: Removes outliers from raster or vector data.
    - `reproject_raster.py`: Reprojects raster data to a different coordinate reference system.
    - `shapefile_to_geojson.py`: Converts shapefiles to GeoJSON format.

## Installation

To get started with this repository, you'll need Python and the required dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/GEOINT-Database.git
cd GEOINT-Database
```

### 2. Install Dependencies

Make sure you have `pip` installed. Then, install the required Python packages by running the following command:

```bash
pip install -r code/analysis_tools/requirements.txt
```

## Usage

### Running the Scripts

The scripts are designed to be run individually, depending on the task you wish to perform. Below are some examples:

1. **Buffer Analysis**

   To perform buffer analysis on vector data, run:

   ```bash
   python code/analysis_tools/buffer_analysis.py
   ```

2. **Geospatial Analysis**

   To perform various geospatial analyses, use the `perform_geospatial_analysis.py` script:

   ```bash
   python code/analysis_tools/perform_geospatial_analysis.py
   ```

3. **Preprocessing Raster Data**

   To clip a raster file by a shapefile, run:

   ```bash
   python code/data_preprocessing/clip_raster_by_shapefile.py
   ```

### Running the UI Program

To run the UI program, use the following command:

```bash
python code/UI_Program/script_runner_UI.Vr.003.py
```

This will launch the graphical user interface (GUI) that allows you to interact with the geospatial analysis tools.

## Documentation

For more detailed information on specific tools and scripts, please refer to the respective documentation files:

- [Geodesic Distance Calculation and Visualization](code/analysis_tools/Geodesic_Distance_Calculation_and_Visualisation.md)

## Troubleshooting

### 1. **ModuleNotFoundError**

   **Problem**: This error occurs when a required Python module is not installed.

   **Solution**: Ensure all dependencies are installed by running:

   ```bash
   pip install -r code/analysis_tools/requirements.txt
   ```

   If the error persists, verify that the module mentioned is included in the `requirements.txt` file and that you are using the correct Python environment.

### 2. **Permission Denied Error**

   **Problem**: You may encounter permission issues when running scripts or accessing files, especially on Linux or macOS.

   **Solution**: Ensure you have the appropriate permissions for the files and directories involved. You can change permissions using:

   ```bash
   chmod +x <filename>
   ```

   Alternatively, you may need to run the command as an administrator (or `sudo` on Unix-like systems).

### 3. **Invalid File Format**

   **Problem**: If you receive errors indicating invalid file formats (e.g., for shapefiles or GeoTIFFs), ensure the input data is in the correct format.

   **Solution**: Verify the format of the input files and ensure they match the expected formats. If converting files, you can use tools like GDAL or QGIS to reformat the files.

### 4. **Script Execution Error**

   **Problem**: If a script fails to execute, check the error message for details on the issue. Common issues include incorrect file paths or missing dependencies.

   **Solution**: Double-check the paths to your input files and ensure all required dependencies are installed. Review the error message to pinpoint the specific issue, and refer to the script documentation or community forums for help.

### 5. **UI Program Not Launching**

   **Problem**: The user interface program may fail to launch due to missing libraries or incorrect Python versions.

   **Solution**: Ensure you have the necessary GUI libraries installed (e.g., Tkinter, PyQt). You may need to install them separately if they aren't included by default in your Python environment.

   ```bash
   pip install tk
   ```

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### The **Troubleshooting** section includes:
- **ModuleNotFoundError**: How to solve issues with missing dependencies.
- **Permission Denied Error**: Fixes for permission-related problems.
- **Invalid File Format**: Suggestions for verifying input file formats.
- **Script Execution Error**: Guidelines to identify and resolve errors during script execution.
- **UI Program Not Launching**: Steps for resolving issues with launching the UI program.

Feel free to modify or add more troubleshooting tips based on common issues users may face!A

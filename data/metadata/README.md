# **Metadata for GEOINT-Database**

Metadata is a critical component of the **GEOINT-Database**, offering essential information about the datasets stored in this repository. It provides context, ensures data accuracy, and enables reproducibility in geospatial analysis.

---

## **Purpose of Metadata**
Metadata in this repository is designed to:
- Document the origin, scope, and accuracy of geospatial datasets.
- Record data transformations and processing workflows.
- Ensure datasets are used in compliance with their respective licenses.

---

## **Metadata Fields**
Each metadata file includes the following fields:

| **Field**              | **Description**                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------|
| **Source**             | Origin of the data (e.g., satellite, drone, field surveys).                                      |
| **Collection Date**    | Date and time when the data was collected.                                                      |
| **Data Type**          | Format of the data (e.g., raster, vector, GPS coordinates).                                      |
| **Description**        | Brief summary of the dataset and its purpose.                                                   |
| **Data Processing**    | Steps taken to clean, transform, or project the data.                                           |
| **Accuracy**           | Precision or known error margin of the dataset (e.g., ±3m).                                     |
| **Resolution**         | Granularity or detail level of the dataset (e.g., "30m cells").                                 |
| **Extent**             | Geographic boundaries of the data (e.g., bounding box: MinX, MinY, MaxX, MaxY).                 |
| **Licensing Restrictions** | Terms of use for the dataset (e.g., CC BY-SA 4.0, Public Domain).                            |

---

## **Example Metadata File**
Here’s an example of a metadata file for a raster dataset:

```json
{
  "source": "Landsat 8",
  "collection_date": "2022-05-01",
  "data_type": "Raster",
  "description": "Satellite imagery of urban areas in the region.",
  "data_processing": "Reprojected from WGS84 to NAD83, clipped to study area.",
  "accuracy": "±3m",
  "resolution": "30m cells",
  "extent": {
    "min_x": -120.0,
    "min_y": 30.0,
    "max_x": -110.0,
    "max_y": 40.0
  },
  "licensing_restrictions": "CC BY-SA 4.0"
}
```

---

## **Metadata Directory Structure**
Metadata files are organized under the `/data/metadata/` directory:

```
GEOINT-Database/
├── data/
│   ├── raw_data/
│   ├── processed_data/
│   └── metadata/
│       ├── README.md
│       ├── dataset_1_metadata.json
│       ├── dataset_2_metadata.json
│       └── ...
```

### **README.md (Metadata Overview)**
The `/data/metadata/README.md` file provides:
- An overview of metadata files.
- Guidelines for creating and updating metadata.
- Examples for structuring metadata files.

---

## **How to Create Metadata**
1. **Use the Example Template:** Copy the structure of the example JSON file above.  
2. **Fill in Relevant Fields:** Include details like source, collection date, data type, accuracy, and processing history.  
3. **Save the File:** Name the file clearly, corresponding to the dataset (e.g., `urban_area_metadata.json`).  
4. **Store in the `/data/metadata/` Directory.**

---

## **Key Metadata Files**
- **README.md:** General guidelines for metadata documentation.  
- Individual metadata files for each dataset in JSON format, such as:
  - `roads_data_metadata.json`
  - `elevation_model_metadata.json`

---

## **Contributing**
We welcome contributions to improve metadata documentation:
- Follow the structure provided in the templates.
- Ensure all fields are filled out with accurate and complete information.
- Submit a pull request with your metadata updates or new files.

---

## **Explore the Metadata**
- [Metadata Directory](data/metadata/)
- [Metadata Documentation Guide](data/metadata/README.md)

---

For questions or assistance, feel free to open an issue in the repository.  
Happy mapping! 🌍

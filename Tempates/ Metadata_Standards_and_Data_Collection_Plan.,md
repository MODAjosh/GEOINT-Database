# Metadata Standards for GEOINT Projects

This document outlines a comprehensive metadata framework for documenting and managing datasets in GEOINT workflows. 

---

## 1. **Metadata Schema**

### Recommended Standards
- **FGDC**: Federal Geographic Data Committee standards for geospatial metadata.
- **ISO 19115**: International standard for metadata used in geographic information.

### Custom Fields (Adaptable per Project Needs)
- Include additional fields to capture project-specific metadata requirements:
  - **Data Sensitivity Level**: Public, Restricted, Confidential.
  - **Processing Stage**: Raw, Preprocessed, Final.
  - **Intended Use**: Analysis type, stakeholders, etc.

---

## 2. **Core Metadata Fields**

### 2.1 Source
- **Definition**: Origin of the dataset.
  - Example: Satellite provider, government agency, open data platform.
- **Format**:
  - Text (e.g., "USGS Earth Explorer").

### 2.2 Timestamp
- **Definition**: Date and time when the dataset was created or acquired.
  - Example: 2025-01-02 14:00 UTC.
- **Format**:
  - ISO 8601 standard (YYYY-MM-DDTHH:mm:ssZ).

### 2.3 Coordinate System
- **Definition**: Spatial reference system used for the dataset.
  - Example: EPSG:4326 (WGS 84).
- **Format**:
  - EPSG code or detailed description (e.g., UTM Zone 33N).

### 2.4 Accuracy
- **Definition**: Precision of spatial data in meters or other units.
  - Example: Horizontal accuracy of 5 meters.
- **Format**:
  - Numeric value with units (e.g., 5m).

---

## 3. **Supplementary Metadata Fields**

### 3.1 Resolution
- **Definition**: Granularity of the data (spatial, temporal, or attribute).
  - Example: Spatial resolution of 30m.
- **Format**:
  - Numeric value with units.

### 3.2 Data Format
- **Definition**: File format of the dataset.
  - Example: GeoTIFF, Shapefile, CSV.
- **Format**:
  - Text (e.g., "GeoTIFF").

### 3.3 Processing History
- **Definition**: Steps applied to the data from acquisition to final format.
  - Example: "Reprojected from EPSG:3857 to EPSG:4326; clipped to area of interest."
- **Format**:
  - Text or structured log.

### 3.4 Licensing and Restrictions
- **Definition**: Terms under which the data can be used or shared.
  - Example: Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Format**:
  - Text or hyperlink.

---

## 4. **Metadata Documentation Best Practices**

### Standardization
- Use consistent terminology and units.
- Adhere to FGDC or ISO 19115 standards wherever applicable.

### Automation
- Generate metadata using scripts or tools when possible (e.g., GDAL for geospatial data).

### Metadata Storage
- Store metadata as:
  - Separate files (e.g., `metadata.json`, `metadata.xml`).
  - Embedded within datasets (e.g., GeoTIFF tags).

### Validation
- Use metadata validation tools to ensure completeness and correctness.
  - Example: PyCSW for ISO 19115 compliance.

---

## 5. **Example Metadata Record**
```json
{
  "source": "Sentinel-2",
  "timestamp": "2025-01-02T14:00:00Z",
  "coordinate_system": "EPSG:4326",
  "accuracy": "10m",
  "resolution": "10m",
  "data_format": "GeoTIFF",
  "processing_history": "Reprojected to EPSG:4326; clipped to AOI.",
  "licensing": "CC BY 4.0",
  "data_sensitivity_level": "Public"
}
```

---

## 6. **Metadata Checklist**

| Field                  | Description                       | Status   |
|------------------------|-----------------------------------|----------|
| Source                | Origin of the dataset            | [ ]      |
| Timestamp             | Date and time of acquisition     | [ ]      |
| Coordinate System     | Spatial reference system          | [ ]      |
| Accuracy              | Precision of spatial data         | [ ]      |
| Resolution            | Granularity of the dataset        | [ ]      |
| Data Format           | File format of the dataset        | [ ]      |
| Processing History    | Steps applied to the data         | [ ]      |
| Licensing Restrictions| Terms of use                      | [ ]      |

---

This metadata framework ensures consistent and comprehensive documentation for GEOINT datasets, supporting reproducibility and data sharing.

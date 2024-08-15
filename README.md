# Reproject-Vector-and-raster-layers

This Python script automates reprojecting selected vector and raster layers in QGIS to a user-defined CRS. It uses the "Reproject Layer" and "Assign Projection" tools, reprojecting layers and adding them as temporary layers, ideal for standardizing spatial data.
Reproject Vector and Raster Layers
This Python script automates the reprojection of selected vector and raster layers in QGIS to a user-defined coordinate reference system (CRS). The script ensures that all selected layers are reprojected and added as temporary layers back into the QGIS project.

**Features**
Vector Layer Reprojection: Uses QGIS's native "Reproject layer" tool to reproject vector layers to a user-defined CRS.
Raster Layer CRS Assignment: Utilizes the GDAL "Assign Projection" tool to assign the specified CRS to raster layers.
Selective Reprojection: Only processes layers that are selected in the QGIS interface.
Temporary Layers: Reprojected layers are added as temporary layers to the QGIS project, preserving the original layers.
Customizable CRS: Easily change the target CRS by specifying a different EPSG code in the script. Commonly used CRS in Australia are listed for convenience.

**Installation**
Download or clone the repository.
Save the script as Reproject_Vector_and_Raster_Layers.py.
Load the script into QGIS using the Python console.

**Usage**
Open your QGIS project.
Select the layers you want to reproject in the Layer Panel.
Open the Python console in QGIS.
Load and run the script.
The selected layers will be reprojected and added as temporary layers in the project.

**Common CRS in Australia**
EPSG:4326: WGS 84 (Global CRS)
EPSG:28355: GDA94 / MGA Zone 55 (Tasmania, Victoria, South Australia)
EPSG:7855: GDA2020 / MGA Zone 55 (Updated Australian CRS)
EPSG:28356: GDA94 / MGA Zone 56 (New South Wales, Queensland)
EPSG:7856: GDA2020 / MGA Zone 56 (Updated Australian CRS)
EPSG:3112: GDA94 / Geoscience Australia Lambert (Australia-wide projection)

**Example**
To reproject selected layers to the EPSG:28355 CRS (GDA94 / MGA Zone 55), simply update the target_crs variable in the script:
Enter on Python--> target_crs = QgsCoordinateReferenceSystem("EPSG:28355")
Then run the script, and the selected layers will be reprojected accordingly.

**Contributing**
If you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request.

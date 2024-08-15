from qgis.core import QgsProject, QgsVectorLayer, QgsRasterLayer, QgsCoordinateReferenceSystem, QgsProcessingFeedback, QgsProcessingContext
import processing

# Define the target CRS (use the EPSG code for your desired CRS)
# Commonly used CRS in Australia:
# - EPSG:4326  - WGS 84 (Global CRS)
# - EPSG:28355 - GDA94 / MGA Zone 55 (Tasmania, Victoria, South Australia)
# - EPSG:7855  - GDA2020 / MGA Zone 55 (Updated Australian CRS)
# - EPSG:28356 - GDA94 / MGA Zone 56 (New South Wales, Queensland)
# - EPSG:7856  - GDA2020 / MGA Zone 56 (Updated Australian CRS)
# - EPSG:3112  - GDA94 / Geoscience Australia Lambert (Australia-wide projection)

target_crs = QgsCoordinateReferenceSystem("EPSG:28355")  # Replace with your target EPSG code

# Initialize feedback for processing (optional, for better logging)
feedback = QgsProcessingFeedback()
context = QgsProcessingContext()

# Get the selected layers in the project
selected_layers = iface.layerTreeView().selectedLayers()

# Iterate over the selected layers
for layer in selected_layers:
    # Reproject vector layers
    if isinstance(layer, QgsVectorLayer):
        layer_name = layer.name()
        print(f"Reprojecting vector layer: {layer_name}")

        # Define parameters for vector reprojection
        params = {
            'INPUT': layer,
            'TARGET_CRS': target_crs.toWkt(),  # Convert CRS to WKT
            'OUTPUT': 'memory:'  # Save reprojected layer in memory
        }

        try:
            # Run the reprojection process for vector layers
            result = processing.run("native:reprojectlayer", params, context=context, feedback=feedback)

            # Check if the result is a layer or a string (file path)
            reprojected_layer = result['OUTPUT']
            if isinstance(reprojected_layer, str):
                reprojected_layer = QgsVectorLayer(reprojected_layer, f"{layer_name}_reprojected", "ogr")

            # Add the reprojected vector layer to the project
            if reprojected_layer.isValid():
                reprojected_layer.setName(f"{layer_name}_reprojected")
                QgsProject.instance().addMapLayer(reprojected_layer)
                print(f"Vector layer reprojected and added to the project: {layer_name}_reprojected")
            else:
                print(f"Failed to reproject vector layer: {layer_name}")

        except Exception as e:
            print(f"Error reprojecting vector layer {layer_name}: {e}")

    # Assign projection to raster layers
    elif isinstance(layer, QgsRasterLayer):
        layer_name = layer.name()
        print(f"Assigning projection to raster layer: {layer_name}")

        # Print source path for debugging
        source_path = layer.source()
        print(f"Raster source path: {source_path}")

        # Define parameters for assigning projection
        params = {
            'INPUT': source_path,
            'CRS': target_crs.toWkt(),  # Assign CRS to WKT
            'OUTPUT': 'memory:'  # Save layer with assigned CRS in memory
        }

        try:
            # Run the assign projection process for raster layers
            result = processing.run("gdal:assignprojection", params, context=context, feedback=feedback)

            # Check if the result is a layer or a string (file path)
            reprojected_layer = result['OUTPUT']
            if isinstance(reprojected_layer, str):
                reprojected_layer = QgsRasterLayer(reprojected_layer, f"{layer_name}_assigned_crs")

            # Add the raster layer with the assigned projection to the project
            if reprojected_layer.isValid():
                reprojected_layer.setName(f"{layer_name}_assigned_crs")
                QgsProject.instance().addMapLayer(reprojected_layer)
                print(f"Raster layer with assigned projection added to the project: {layer_name}_assigned_crs")
            else:
                print(f"Failed to assign projection to raster layer: {layer_name}")

        except Exception as e:
            print(f"Error assigning projection to raster layer {layer_name}: {e}")

    else:
        print(f"Skipping unsupported layer type: {layer.name()}")

# GIS-DEVELOPER-S

# Application 1



## GIS Web App

This repository contains the source code for a GIS Web App that allows users to interact with spatial data on an interactive map. The app is built using HTML, CSS, and JavaScript, with Leaflet as the mapping library and additional plugins for drawing and geocoding functionalities.

### Features

1. Map Layers:
   - OpenStreetMap and Esri Satellite imagery are available as base maps.
   - Users can switch between base maps using the layer control.

2. Spatial Data Editing:
   - Drawing functionalities for creating points, lines, polygons, rectangles, and circles on the map.
   - Editing and deleting drawn features are supported.

3. Search Bar:
   - Users can search for locations using the search bar, powered by Esri geocoding.

4. Spatial Data Upload:
   - A file input allows users to upload GeoJSON, KML, or Shapefile data.
   - The uploaded data is parsed and added to the map.

### How to Use


1. Open the HTML File:
   - Open the gis.html file in your preferred web browser.

2. Interact with the App:
   - Explore the map, switch between base maps, and use the drawing tools.
   - Test the search functionality by entering addresses in the search bar.
   - Upload spatial data files and observe them displayed on the map.

### Credits

- Leaflet: [Leaflet](https://leafletjs.com/)
- Leaflet Draw Plugin: [Leaflet.draw](https://github.com/Leaflet/Leaflet.draw)
- Esri Leaflet: [Esri Leaflet](https://esri.github.io/esri-leaflet/)
- Esri Leaflet Geocoder: [Esri Leaflet Geocoder](https://github.com/Esri/esri-leaflet-geocoder)


# Application 2


# Raster Viewer

This repository contains RasterViewer.ipynb which provide interactive graphical interfaces for visualizing raster and GIS data, respectively. Additionally, Jupyter Notebooks (RasterViewer.ipynb ) are available for each script, offering a more interactive and step-by-step exploration of the functionalities.

## Raster Viewer

### Features

- Load raster data (TIFF files).
- Visualize raster data using different band combinations (RGB, Red, Green, Blue).
- Apply filters, calculate statistics, and apply mathematical transformations to raster data.
- Zoom and pan functionalities for exploring the raster image.

### Libraries Used

- matplotlib: For creating plots and visualizing raster data.
- rasterio: For reading and processing raster data.
- numpy: For numerical operations.
- tkinter: For creating the graphical user interface.

### How to Use


1. Click "Load Raster" to select a TIFF file.
2. Explore different band combinations and apply filters or transformations.
3. Use the zoom and pan functionalities for detailed examination.

## Shape file(.shp) upload

### Features

- Load shapefile data.
- Visualize shapefile data on an interactive map.
- Show attribute charts for selected columns in the shapefile.
- Zoom and pan functionalities for exploring the map.

### Libraries Used

- matplotlib: For creating plots and visualizing shapefile data.
- geopandas: For reading and processing shapefile data.
- tkinter: For creating the graphical user interface.

### How to Use

1. Run the  script.
2. Click "Load Shapefile" to select a shapefile.
3. Visualize the shapefile data on the map.
4. Click "Show Attribute Chart" to explore attribute distribution.

## Jupyter Notebooks

The Jupyter Notebooks (RasterViewer.ipynb ) provide an interactive environment to run and experiment with the code step by step. These notebooks include detailed explanations and visualizations of the functionalities provided by the scripts.

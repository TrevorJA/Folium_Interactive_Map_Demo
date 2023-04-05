
## Creating Interactive Geospatial Maps in Python with Folium

This repository hosts demonstration code for a blog post: [Waterprogramming, *Creating Interactive Geospatial Maps in Python with Folium*.]()

In this post, I provide a demonstration on how to use the `folium` package to create an HTML based interactive map of a hydrologic watershed.

## Demo: Mapping a hydrologic basin data with Folium

All of the code and data used in this post is located in a GitHub repository: [trevorja/Folium_Interactive_Map_Demo.](https://github.com/TrevorJA/Folium_Interactive_Map_Demo)

To interact with the demo map directly, download the file here: [`basin_map.html`](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/blob/main/basin_map.html)

The [`folium_map_demo.ipynb`](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/blob/main/folium_map_demo.ipynb) walks through the process shown below and will re-create the map shown above. You can create a similar plot for a different basin by changing the `station_id` number inside ['retrieve_basin_data.ipynb'](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/blob/main/retrieve_basin_data.ipynb) to a specific USGS gauge of interest. 

Here is a brief video showcasing the interaction with the final map:

![interactive_map_usage.gif](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/tree/main/images/interactive_map_usage.gif)


### Map Data

For this demo, I am plotting various features within a hydrologic basin in northern New Mexico. 

All of the data in the map is retrieved using the [`pynhd`](https://github.com/hyriver/pynhd) package from the [HyRiver](https://hyriver.readthedocs.io/en/latest/) suite for python. For more information about these packages, see my previous post, [*Efficient hydroclimatic data accessing with HyRiver for Python*.](https://waterprogramming.wordpress.com/2022/09/20/efficient-hydroclimatic-data-accessing-with-hyriver-for-python/)

The script ['retrieve_basin_data.ipynb'](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/blob/main/retrieve_basin_data.ipynb) is set up to retrieve several features from the basin, including:
- Basin boundary
- Mainstem river
- Tributary rivers
- USGS gauge locations
- New Mexico Water Data Initiative (NMWDI) Sites
- HUC12 pour points

The geospatial data (longitude and latitudes) for each of these features are exported to [`data/basin_data.csv`](https://github.com/TrevorJA/Folium_Interactive_Map_Demo/blob/main/data/basin_data.csv) and used later to generate the folium map.
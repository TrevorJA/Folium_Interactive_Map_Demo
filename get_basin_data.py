"""
Pynhd data retrieval methods derived from: https://pygeohydro.readthedocs.io/en/latest/examples/nhdplus.html
"""

import pynhd as nhd
from pynhd import NLDI, NHDPlusHR, WaterData

station_id = "01031500"

# Initialize the NLDI retrieval tool
nldi = NLDI()

# Find the basin upstream of the station
basin = nldi.get_basins(station_id)

# Find the main flow line
main_flow = nldi.navigate_byid(
    fsource="nwissite",
    fid=f"USGS-{station_id}",
    navigation="upstreamMain",
    source="flowlines",
    distance=1000)

tributary_flow = nldi.navigate_byid(
    fsource="nwissite",
    fid=f"USGS-{station_id}",
    navigation="upstreamTributaries",
    source="flowlines",
    distance=1000)

all_stations = nldi.navigate_byid(
    fsource="nwissite",
    fid=f"USGS-{station_id}",
    navigation="upstreamTributaries",
    source="nwissite",
    distance=1000)

pour_points = nldi.navigate_byid(
    fsource="nwissite",
    fid=f"USGS-{station_id}",
    navigation="upstreamTributaries",
    source="huc12pp",
    distance=1000)


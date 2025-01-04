import arcpy 

# IDW
with arcpy.EnvManager(scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Idw(
        in_point_features="SaudiWeatherFeature",
        z_field="temperature_2m_mean",
        cell_size=0.054779084,
        power=2,
        search_radius="VARIABLE 12",
        in_barrier_polyline_features=None
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_Weather_IDW")


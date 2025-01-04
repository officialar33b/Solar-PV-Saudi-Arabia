import arcpy

# Calculating Euclidean Distance Raster
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', mask="saudi_shp", scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_distance_raster = arcpy.sa.EucDistance(
        in_source_data="SaudiGridLines",
        maximum_distance=None,
        cell_size=0.0025,
        out_direction_raster=None,
        distance_method="PLANAR",
        in_barrier_data=None,
        out_back_direction_raster=None
    )
    out_distance_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_Euclidean_Distance_Grid")

# Reclassify Tool.
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Saudi_Euclidean_Distance_Grid",
        reclass_field="VALUE",
        remap="0 0.502428 10;0.502428 1.004857 9;1.004857 1.507285 8;1.507285 2.009714 7;2.009714 2.512142 6;2.512142 3.014571 5;3.014571 3.516999 4;3.516999 4.019427 3;4.019427 4.521856 2;4.521856 5.024284 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Grid_Reclassify")
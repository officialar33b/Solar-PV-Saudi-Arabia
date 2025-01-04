import arcpy

# Calculating Euclidean Distance Raster
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', mask="saudi_shp", scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_distance_raster = arcpy.sa.EucDistance(
        in_source_data="saudi_arabia_highway",
        maximum_distance=100,
        cell_size=0.0025,
        out_direction_raster=None,
        distance_method="PLANAR",
        in_barrier_data=None,
        out_back_direction_raster=None
    )
    out_distance_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_Euclidean_Distance_Roads")

# Reclassify Tool.
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Saudi_Euclidean_Distance_Roads",
        reclass_field="VALUE",
        remap="0 0.115123 10;0.115123 0.306994 9;0.306994 0.524447 8;0.524447 0.793067 7;0.793067 1.087269 6;1.087269 1.432637 5;1.432637 1.816379 4;1.816379 2.225703 3;2.225703 2.660611 2;2.660611 3.261806 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Roads_Reclass")
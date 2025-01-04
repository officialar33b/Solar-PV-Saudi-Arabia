import arcpy

# Calculating the slope using Saudi_DEM_Clip raster in the gdb.
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Slope(
        in_raster="Saudi_DEM_Clip",
        output_measurement="DEGREE",
        z_factor=1,
        method="PLANAR",
        z_unit="METER",
        analysis_target_device="GPU_THEN_CPU"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_slope")

# Reclassify Tool.
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Saudi_slope",
        reclass_field="VALUE",
        remap="0 4.776067 10;4.776067 9.552133 9;9.552133 14.328200 8;14.328200 19.104266 7;19.104266 23.880333 6;23.880333 28.656400 5;28.656400 33.432466 4;33.432466 38.208533 3;38.208533 42.984599 2;42.984599 47.760666 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Slope_reclassify")
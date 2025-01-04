import arcpy
 
# Calculating Aspect using aspect tool.
with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025):
    arcpy.ddd.Aspect(
        in_raster="Saudi_DEM_Clip",
        out_raster=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_Aspect",
        method="PLANAR",
        z_unit="METER",
        project_geodesic_azimuths="GEODESIC_AZIMUTHS",
        analysis_target_device="GPU_THEN_CPU"
    )

# Reclassify Tool.

with arcpy.EnvManager(outputCoordinateSystem='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]', cellSize=0.0025, scratchWorkspace=r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb"):
    out_raster = arcpy.sa.Reclassify(
        in_raster="Saudi_Aspect",
        reclass_field="VALUE",
        remap="-1 7;-1 22.500000 1;22.500000 67.500000 2;67.500000 112.500000 4;112.500000 157.500000 8;157.500000 202.500000 10;202.500000 247.500000 8;247.500000 292.500000 4;292.500000 337.500000 2;337.500000 360 1",
        missing_values="DATA"
    )
    out_raster.save(r"C:\Users\areeb\Documents\GIST 498\Saudi Elevation\Saudi Solar Proper\Saudi Solar Proper.gdb\Saudi_Aspect_Reclass")